from typing import Iterable, List, Optional, Union
import torch.multiprocessing as mp
import torch
from typing import List, Union
from ctypes import c_bool
from scipy.signal import resample
from scipy import signal
import faster_whisper
import collections
import numpy as np
import pvporcupine
import traceback
import threading
import webrtcvad
import itertools
import platform
import pyaudio
import logging
import struct
import halo
import time
import copy
import os
import re
import gc

INIT_MODEL_TRANSCRIPTION = "large-v3"
INIT_MODEL_TRANSCRIPTION_REALTIME = "large-v3"
INIT_REALTIME_PROCESSING_PAUSE = 0.2
INIT_SILERO_SENSITIVITY = 0.4
INIT_WEBRTC_SENSITIVITY = 3
INIT_POST_SPEECH_SILENCE_DURATION = 0.6
INIT_MIN_LENGTH_OF_RECORDING = 0.5
INIT_MIN_GAP_BETWEEN_RECORDINGS = 0
INIT_WAKE_WORDS_SENSITIVITY = 0.6
INIT_PRE_RECORDING_BUFFER_DURATION = 1.0
INIT_WAKE_WORD_ACTIVATION_DELAY = 0.0
INIT_WAKE_WORD_TIMEOUT = 5.0
ALLOWED_LATENCY_LIMIT = 10

TIME_SLEEP = 0.02
SAMPLE_RATE = 16000
BUFFER_SIZE = 512
INT16_MAX_ABS_VALUE = 32768.0

INIT_HANDLE_BUFFER_OVERFLOW = False
if platform.system() != 'Darwin':
    INIT_HANDLE_BUFFER_OVERFLOW = True


class PyloomASR:

    def __init__(self,
                 model: str = INIT_MODEL_TRANSCRIPTION,
                 language: str = "",
                 compute_type: str = "default",
                 input_device_index: int = 0,
                 gpu_device_index: Union[int, List[int]] = 0,
                 on_recording_start=None,
                 on_recording_stop=None,
                 on_transcription_start=None,
                 ensure_sentence_starting_uppercase=True,
                 ensure_sentence_ends_with_period=True,
                 use_microphone=False,
                 spinner=False,
                 level=logging.WARNING,

                 enable_realtime_transcription=True,
                 realtime_model_type=INIT_MODEL_TRANSCRIPTION_REALTIME,
                 realtime_processing_pause=INIT_REALTIME_PROCESSING_PAUSE,
                 on_realtime_transcription_update=None,
                 on_realtime_transcription_stabilized=None,

                 silero_sensitivity: float = INIT_SILERO_SENSITIVITY,
                 silero_use_onnx: bool = False,
                 webrtc_sensitivity: int = INIT_WEBRTC_SENSITIVITY,
                 post_speech_silence_duration: float = (
                     INIT_POST_SPEECH_SILENCE_DURATION
                 ),
                 min_length_of_recording: float = (
                     INIT_MIN_LENGTH_OF_RECORDING
                 ),
                 min_gap_between_recordings: float = (
                     INIT_MIN_GAP_BETWEEN_RECORDINGS
                 ),
                 pre_recording_buffer_duration: float = (
                     INIT_PRE_RECORDING_BUFFER_DURATION
                 ),
                 on_vad_detect_start=None,
                 on_vad_detect_stop=None,

                 wake_words: str = "",
                 wake_words_sensitivity: float = INIT_WAKE_WORDS_SENSITIVITY,
                 wake_word_activation_delay: float = (
                    INIT_WAKE_WORD_ACTIVATION_DELAY
                 ),
                 wake_word_timeout: float = INIT_WAKE_WORD_TIMEOUT,
                 on_wakeword_detected=None,
                 on_wakeword_timeout=None,
                 on_wakeword_detection_start=None,
                 on_wakeword_detection_end=None,
                 on_recorded_chunk=None,
                 debug_mode=True,
                 handle_buffer_overflow: bool = INIT_HANDLE_BUFFER_OVERFLOW,
                 beam_size: int = 5,
                 beam_size_realtime: int = 3,
                 buffer_size: int = BUFFER_SIZE,
                 sample_rate: int = SAMPLE_RATE,
                 initial_prompt: Optional[Union[str, Iterable[int]]] = None,
                 suppress_tokens: Optional[List[int]] = [-1],
                 ):
  
        self.language = language
        self.compute_type = compute_type
        self.input_device_index = input_device_index
        self.gpu_device_index = gpu_device_index
        self.wake_words = wake_words
        self.wake_word_activation_delay = wake_word_activation_delay
        self.wake_word_timeout = wake_word_timeout
        self.ensure_sentence_starting_uppercase = (
            ensure_sentence_starting_uppercase
        )
        self.ensure_sentence_ends_with_period = (
            ensure_sentence_ends_with_period
        )
        self.use_microphone = mp.Value(c_bool, use_microphone)
        self.min_gap_between_recordings = min_gap_between_recordings
        self.min_length_of_recording = min_length_of_recording
        self.pre_recording_buffer_duration = pre_recording_buffer_duration
        self.post_speech_silence_duration = post_speech_silence_duration
        self.on_recording_start = on_recording_start
        self.on_recording_stop = on_recording_stop
        self.on_wakeword_detected = on_wakeword_detected
        self.on_wakeword_timeout = on_wakeword_timeout
        self.on_vad_detect_start = on_vad_detect_start
        self.on_vad_detect_stop = on_vad_detect_stop
        self.on_wakeword_detection_start = on_wakeword_detection_start
        self.on_wakeword_detection_end = on_wakeword_detection_end
        self.on_recorded_chunk = on_recorded_chunk
        self.on_transcription_start = on_transcription_start
        self.enable_realtime_transcription = enable_realtime_transcription
        self.realtime_model_type = realtime_model_type
        self.realtime_processing_pause = realtime_processing_pause
        self.on_realtime_transcription_update = (
            on_realtime_transcription_update
        )
        self.on_realtime_transcription_stabilized = (
            on_realtime_transcription_stabilized
        )
        self.debug_mode = debug_mode
        self.handle_buffer_overflow = handle_buffer_overflow
        self.beam_size = beam_size
        self.beam_size_realtime = beam_size_realtime
        self.allowed_latency_limit = ALLOWED_LATENCY_LIMIT

        self.level = level
        self.audio_queue = mp.Queue()
        self.buffer_size = buffer_size
        self.sample_rate = sample_rate
        self.recording_start_time = 0
        self.recording_stop_time = 0
        self.wake_word_detect_time = 0
        self.silero_check_time = 0
        self.silero_working = False
        self.speech_end_silence_start = 0
        self.silero_sensitivity = silero_sensitivity
        self.listen_start = 0
        self.spinner = spinner
        self.halo = None
        self.state = "inactive"
        self.wakeword_detected = False
        self.text_storage = []
        self.realtime_stabilized_text = ""
        self.realtime_stabilized_safetext = ""
        self.is_webrtc_speech_active = False
        self.is_silero_speech_active = False
        self.recording_thread = None
        self.realtime_thread = None
        self.audio_interface = None
        self.audio = None
        self.stream = None
        self.start_recording_event = threading.Event()
        self.stop_recording_event = threading.Event()
        self.last_transcription_bytes = None
        self.initial_prompt = initial_prompt
        self.suppress_tokens = suppress_tokens

        log_format = 'RealTimeSTT: %(name)s - %(levelname)s - %(message)s'

        logger = logging.getLogger()
        logger.setLevel(level)

        file_handler = logging.FileHandler('realtimesst.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(log_format))

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(logging.Formatter(log_format))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        self.is_shut_down = False
        self.shutdown_event = mp.Event()

        logging.info("Starting RealTimeSTT")

        try:
            if mp.get_start_method(allow_none=True) is None:
                mp.set_start_method("spawn")
        except RuntimeError as e:
            print("Start method has already been set. Details:", e)

        self.interrupt_stop_event = mp.Event()
        self.was_interrupted = mp.Event()
        self.main_transcription_ready_event = mp.Event()
        self.parent_transcription_pipe, child_transcription_pipe = mp.Pipe()

        self.transcript_process = mp.Process(
            target=PyloomASR._transcription_worker,
            args=(
                child_transcription_pipe,
                model,
                self.compute_type,
                self.gpu_device_index,
                self.main_transcription_ready_event,
                self.shutdown_event,
                self.interrupt_stop_event,
                self.beam_size,
                self.initial_prompt,
                self.suppress_tokens
            )
        )
        self.transcript_process.start()

        if self.use_microphone.value:
            logging.info("Initializing audio recording"
                         " (creating pyAudio input stream,"
                         f" sample rate: {self.sample_rate}"
                         f" buffer size: {self.buffer_size}"
                         )
            self.reader_process = mp.Process(
                target=PyloomASR._audio_data_worker,
                args=(
                    self.audio_queue,
                    self.sample_rate,
                    self.buffer_size,
                    self.input_device_index,
                    self.shutdown_event,
                    self.interrupt_stop_event,
                    self.use_microphone
                )
            )
            # self.reader_process.start()

        if self.enable_realtime_transcription:
            try:
                logging.info("Initializing faster_whisper realtime "
                             f"transcription model {self.realtime_model_type}"
                             )
                self.realtime_model_type = faster_whisper.WhisperModel(
                    model_size_or_path=self.realtime_model_type,
                    device='cuda' if torch.cuda.is_available() else 'cpu',
                    compute_type=self.compute_type,
                    device_index=self.gpu_device_index
                )

            except Exception as e:
                logging.exception("Error initializing faster_whisper "
                                  f"realtime transcription model: {e}"
                                  )
                raise

            logging.debug("Faster_whisper realtime speech to text "
                          "transcription model initialized successfully")

        if wake_words:

            self.wake_words_list = [
                word.strip() for word in wake_words.lower().split(',')
            ]
            sensitivity_list = [
                float(wake_words_sensitivity)
                for _ in range(len(self.wake_words_list))
            ]

            try:
                self.porcupine = pvporcupine.create(
                    keywords=self.wake_words_list,
                    sensitivities=sensitivity_list
                )
                self.buffer_size = self.porcupine.frame_length
                self.sample_rate = self.porcupine.sample_rate

            except Exception as e:
                logging.exception("Error initializing porcupine "
                                  f"wake word detection engine: {e}"
                                  )
                raise

            logging.debug("Porcupine wake word detection "
                          "engine initialized successfully"
                          )

        try:
            logging.info("Initializing WebRTC voice with "
                         f"Sensitivity {webrtc_sensitivity}"
                         )
            self.webrtc_vad_model = webrtcvad.Vad()
            self.webrtc_vad_model.set_mode(webrtc_sensitivity)

        except Exception as e:
            logging.exception("Error initializing WebRTC voice "
                              f"activity detection engine: {e}"
                              )
            raise

        logging.debug("WebRTC VAD voice activity detection "
                      "engine initialized successfully"
                      )

        try:
            self.silero_vad_model, _ = torch.hub.load(
                repo_or_dir="snakers4/silero-vad",
                model="silero_vad",
                verbose=False,
                onnx=silero_use_onnx
            )

        except Exception as e:
            logging.exception(f"Error initializing Silero VAD "
                              f"voice activity detection engine: {e}"
                              )
            raise

        logging.debug("Silero VAD voice activity detection "
                      "engine initialized successfully"
                      )

        self.audio_buffer = collections.deque(
            maxlen=int((self.sample_rate // self.buffer_size) *
                       self.pre_recording_buffer_duration)
        )
        self.frames = []

        self.is_recording = False
        self.is_running = True
        self.start_recording_on_voice_activity = False
        self.stop_recording_on_voice_deactivity = False

        self.recording_thread = threading.Thread(target=self._recording_worker)
        self.recording_thread.daemon = True
        self.recording_thread.start()

        self.realtime_thread = threading.Thread(target=self._realtime_worker)
        self.realtime_thread.daemon = True
        self.realtime_thread.start()

        logging.debug('Waiting for main transcription model to start')
        self.main_transcription_ready_event.wait()
        logging.debug('Main transcription model ready')

        logging.debug('RealtimeSTT initialization completed successfully')

    @staticmethod
    def _transcription_worker(conn,
                              model_path,
                              compute_type,
                              gpu_device_index,
                              ready_event,
                              shutdown_event,
                              interrupt_stop_event,
                              beam_size,
                              initial_prompt,
                              suppress_tokens
                              ):
        logging.info("Initializing faster_whisper "
                     f"main transcription model {model_path}"
                     )

        try:
            model = faster_whisper.WhisperModel(
                model_size_or_path=model_path,
                device='cuda' if torch.cuda.is_available() else 'cpu',
                compute_type=compute_type,
                device_index=gpu_device_index,
            )

        except Exception as e:
            logging.exception("Error initializing main "
                              f"faster_whisper transcription model: {e}"
                              )
            raise

        ready_event.set()

        logging.debug("Faster_whisper main speech to text "
                      "transcription model initialized successfully"
                      )

        while not shutdown_event.is_set():
            try:
                if conn.poll(0.5):
                    audio, language = conn.recv()
                    try:
                        segments = model.transcribe(
                            audio,
                            language=language if language else None,
                            beam_size=beam_size,
                            initial_prompt=initial_prompt,
                            suppress_tokens=suppress_tokens
                        )
                        segments = segments[0]
                        transcription = " ".join(seg.text for seg in segments)
                        transcription = transcription.strip()
                        conn.send(('success', transcription))
                    except Exception as e:
                        logging.error(f"General transcription error: {e}")
                        conn.send(('error', str(e)))
                else:
                    # If there's no data, sleep / prevent busy waiting
                    time.sleep(0.02)
            except KeyboardInterrupt:
                interrupt_stop_event.set()
                logging.debug("Transcription worker process "
                              "finished due to KeyboardInterrupt"
                              )
                break

    @staticmethod
    def _audio_data_worker(audio_queue,
                           sample_rate,
                           buffer_size,
                           input_device_index,
                           shutdown_event,
                           interrupt_stop_event,
                           use_microphone):
        try:
            audio_interface = pyaudio.PyAudio()
            stream = audio_interface.open(
                rate=sample_rate,
                format=pyaudio.paInt16,
                channels=1,
                input=True,
                frames_per_buffer=buffer_size,
                input_device_index=input_device_index,
                )

        except Exception as e:
            logging.exception("Error initializing pyaudio "
                              f"audio recording: {e}"
                              )
            raise

        logging.debug("Audio recording (pyAudio input "
                      "stream) initialized successfully"
                      )

        try:
            while not shutdown_event.is_set():
                try:
                    data = stream.read(buffer_size)

                except OSError as e:
                    if e.errno == pyaudio.paInputOverflowed:
                        logging.warning("Input overflowed. Frame dropped.")
                    else:
                        logging.error(f"Error during recording: {e}")
                    tb_str = traceback.format_exc()
                    print(f"Traceback: {tb_str}")
                    print(f"Error: {e}")
                    continue

                except Exception as e:
                    logging.error(f"Error during recording: {e}")
                    tb_str = traceback.format_exc()
                    print(f"Traceback: {tb_str}")
                    print(f"Error: {e}")
                    continue

                if use_microphone.value:
                    audio_queue.put(data)

        except KeyboardInterrupt:
            interrupt_stop_event.set()
            logging.debug("Audio data worker process "
                          "finished due to KeyboardInterrupt"
                          )
        finally:
            stream.stop_stream()
            stream.close()
            audio_interface.terminate()

    def wakeup(self):
        self.listen_start = time.time()

    def abort(self):
        self.start_recording_on_voice_activity = False
        self.stop_recording_on_voice_deactivity = False
        self._set_state("inactive")
        self.interrupt_stop_event.set()
        self.was_interrupted.wait()
        self.was_interrupted.clear()

    def wait_audio(self):
        self.listen_start = time.time()

        if not self.is_recording and not self.frames:
            self._set_state("listening")
            self.start_recording_on_voice_activity = True

            while not self.interrupt_stop_event.is_set():
                if self.start_recording_event.wait(timeout=0.02):
                    break

        if self.is_recording:
            self.stop_recording_on_voice_deactivity = True

            while not self.interrupt_stop_event.is_set():
                if (self.stop_recording_event.wait(timeout=0.02)):
                    break

        audio_array = np.frombuffer(b''.join(self.frames), dtype=np.int16)
        self.audio = audio_array.astype(np.float32) / INT16_MAX_ABS_VALUE
        self.frames.clear()

        self.recording_stop_time = 0
        self.listen_start = 0

        self._set_state("inactive")

    def transcribe(self):
        self._set_state("transcribing")
        audio_copy = copy.deepcopy(self.audio)
        self.parent_transcription_pipe.send((self.audio, self.language))
        status, result = self.parent_transcription_pipe.recv()

        self._set_state("inactive")
        if status == 'success':
            self.last_transcription_bytes = audio_copy
            return self._preprocess_output(result)
        else:
            logging.error(result)
            raise Exception(result)

    def text(self,
             on_transcription_finished=None,
             ):
        self.interrupt_stop_event.clear()
        self.was_interrupted.clear()

        self.wait_audio()

        if self.is_shut_down or self.interrupt_stop_event.is_set():
            if self.interrupt_stop_event.is_set():
                self.was_interrupted.set()
            return ""

        if on_transcription_finished:
            threading.Thread(target=on_transcription_finished,
                             args=(self.transcribe(),)).start()
        else:
            return self.transcribe()

    def start(self):
        if (time.time() - self.recording_stop_time
                < self.min_gap_between_recordings):
            logging.info("Attempted to start recording "
                         "too soon after stopping."
                         )
            return self

        logging.info("recording started")
        self._set_state("recording")
        self.text_storage = []
        self.realtime_stabilized_text = ""
        self.realtime_stabilized_safetext = ""
        self.wakeword_detected = False
        self.wake_word_detect_time = 0
        self.frames = []
        self.is_recording = True
        self.recording_start_time = time.time()
        self.is_silero_speech_active = False
        self.is_webrtc_speech_active = False
        self.stop_recording_event.clear()
        self.start_recording_event.set()

        if self.on_recording_start:
            self.on_recording_start()

        return self

    def stop(self):
        if (time.time() - self.recording_start_time
                < self.min_length_of_recording):
            logging.info("Attempted to stop recording "
                         "too soon after starting."
                         )
            return self

        logging.info("recording stopped")
        self.is_recording = False
        self.recording_stop_time = time.time()
        self.is_silero_speech_active = False
        self.is_webrtc_speech_active = False
        self.silero_check_time = 0
        self.start_recording_event.clear()
        self.stop_recording_event.set()

        if self.on_recording_stop:
            self.on_recording_stop()

        return self

    def feed_audio(self, chunk, original_sample_rate=16000):
        if not hasattr(self, 'buffer'):
            self.buffer = bytearray()

        if isinstance(chunk, np.ndarray):
            if chunk.ndim == 2:
                chunk = np.mean(chunk, axis=1)

            if original_sample_rate != 16000:
                num_samples = int(len(chunk) * 16000 / original_sample_rate)
                chunk = resample(chunk, num_samples)
            chunk = chunk.astype(np.int16)
            chunk = chunk.tobytes()

        self.buffer += chunk
        buf_size = 2 * self.buffer_size  # silero complains if too short

        while len(self.buffer) >= buf_size:
            to_process = self.buffer[:buf_size]
            self.buffer = self.buffer[buf_size:]
            self.audio_queue.put(to_process)

    def set_microphone(self, microphone_on=True):
        logging.info("Setting microphone to: " + str(microphone_on))
        self.use_microphone.value = microphone_on

    def shutdown(self):
        self.is_shut_down = True
        self.start_recording_event.set()
        self.stop_recording_event.set()

        self.shutdown_event.set()
        self.is_recording = False
        self.is_running = False

        logging.debug('Finishing recording thread')
        if self.recording_thread:
            self.recording_thread.join()

        logging.debug('Terminating reader process')

        if self.use_microphone:
            self.reader_process.join(timeout=10)

        if self.reader_process.is_alive():
            logging.warning("Reader process did not terminate "
                            "in time. Terminating forcefully."
                            )
            self.reader_process.terminate()

        logging.debug('Terminating transcription process')
        self.transcript_process.join(timeout=10)

        if self.transcript_process.is_alive():
            logging.warning("Transcript process did not terminate "
                            "in time. Terminating forcefully."
                            )
            self.transcript_process.terminate()

        self.parent_transcription_pipe.close()

        logging.debug('Finishing realtime thread')
        if self.realtime_thread:
            self.realtime_thread.join()

        if self.enable_realtime_transcription:
            if self.realtime_model_type:
                del self.realtime_model_type
                self.realtime_model_type = None
        gc.collect()

    def _recording_worker(self):
        logging.debug('Starting recording worker')
        try:
            was_recording = False
            delay_was_passed = False

            while self.is_running:

                try:

                    data = self.audio_queue.get()
                    if self.on_recorded_chunk:
                        self.on_recorded_chunk(data)

                    if self.handle_buffer_overflow:
                        if (self.audio_queue.qsize() >
                                self.allowed_latency_limit):
                            logging.warning("Audio queue size exceeds "
                                            "latency limit. Current size: "
                                            f"{self.audio_queue.qsize()}. "
                                            "Discarding old audio chunks."
                                            )

                        while (self.audio_queue.qsize() >
                                self.allowed_latency_limit):

                            data = self.audio_queue.get()

                except BrokenPipeError:
                    print("BrokenPipeError _recording_worker")
                    self.is_running = False
                    break

                if not self.is_recording:
                    time_since_listen_start = (time.time() - self.listen_start
                                               if self.listen_start else 0)

                    wake_word_activation_delay_passed = (
                        time_since_listen_start >
                        self.wake_word_activation_delay
                    )

                    if wake_word_activation_delay_passed \
                            and not delay_was_passed:

                        if self.wake_words and self.wake_word_activation_delay:
                            if self.on_wakeword_timeout:
                                self.on_wakeword_timeout()
                    delay_was_passed = wake_word_activation_delay_passed

                    if not self.recording_stop_time:
                        if self.wake_words \
                                and wake_word_activation_delay_passed \
                                and not self.wakeword_detected:
                            self._set_state("wakeword")
                        else:
                            if self.listen_start:
                                self._set_state("listening")
                            else:
                                self._set_state("inactive")

                    if self.wake_words and wake_word_activation_delay_passed:
                        try:
                            pcm = struct.unpack_from(
                                "h" * self.buffer_size,
                                data
                                )
                            wakeword_index = self.porcupine.process(pcm)

                        except struct.error:
                            logging.error("Error unpacking audio data "
                                          "for wake word processing.")
                            continue

                        except Exception as e:
                            logging.error(f"Wake word processing error: {e}")
                            continue

                        if wakeword_index >= 0:

                            samples_for_0_1_sec = int(self.sample_rate * 0.1)
                            start_index = max(
                                0,
                                len(self.audio_buffer) - samples_for_0_1_sec
                                )
                            temp_samples = collections.deque(
                                itertools.islice(
                                    self.audio_buffer,
                                    start_index,
                                    None)
                                )
                            self.audio_buffer.clear()
                            self.audio_buffer.extend(temp_samples)

                            self.wake_word_detect_time = time.time()
                            self.wakeword_detected = True
                            if self.on_wakeword_detected:
                                self.on_wakeword_detected()

                    if ((not self.wake_words
                         or not wake_word_activation_delay_passed)
                            and self.start_recording_on_voice_activity) \
                            or self.wakeword_detected:

                        if self._is_voice_active():
                            logging.info("voice activity detected")

                            self.start()

                            if self.is_recording:
                                self.start_recording_on_voice_activity = False
                                self.frames.extend(list(self.audio_buffer))
                                self.audio_buffer.clear()

                            self.silero_vad_model.reset_states()
                        else:
                            data_copy = data[:]
                            self._check_voice_activity(data_copy)

                    self.speech_end_silence_start = 0

                else:
                    if self.stop_recording_on_voice_deactivity:

                        if not self._is_webrtc_speech(data, True):
                            if self.speech_end_silence_start == 0:
                                self.speech_end_silence_start = time.time()

                        else:
                            self.speech_end_silence_start = 0

                        # Wait for silence to stop recording after speech
                        if self.speech_end_silence_start and time.time() - \
                                self.speech_end_silence_start > \
                                self.post_speech_silence_duration:
                            logging.info("voice deactivity detected")
                            self.stop()

                if not self.is_recording and was_recording:
                    self.stop_recording_on_voice_deactivity = False

                if time.time() - self.silero_check_time > 0.1:
                    self.silero_check_time = 0

                if self.wake_word_detect_time and time.time() - \
                        self.wake_word_detect_time > self.wake_word_timeout:

                    self.wake_word_detect_time = 0
                    if self.wakeword_detected and self.on_wakeword_timeout:
                        self.on_wakeword_timeout()
                    self.wakeword_detected = False

                was_recording = self.is_recording

                if self.is_recording:
                    self.frames.append(data)

                if not self.is_recording or self.speech_end_silence_start:
                    self.audio_buffer.append(data)

        except Exception as e:
            if not self.interrupt_stop_event.is_set():
                logging.error(f"Unhandled exeption in _recording_worker: {e}")
                raise

    def _realtime_worker(self):
        try:
            logging.debug('Starting realtime worker')

            if not self.enable_realtime_transcription:
                return

            while self.is_running:
                if self.is_recording:
                    time.sleep(self.realtime_processing_pause)

                    audio_array = np.frombuffer(
                        b''.join(self.frames),
                        dtype=np.int16
                        )

                    audio_array = audio_array.astype(np.float32) / \
                        INT16_MAX_ABS_VALUE

                    segments = self.realtime_model_type.transcribe(
                        audio_array,
                        language=self.language if self.language else None,
                        beam_size=self.beam_size_realtime,
                        initial_prompt=self.initial_prompt,
                        suppress_tokens=self.suppress_tokens,
                    )

                    if self.is_recording and time.time() - \
                            self.recording_start_time > 0.5:

                        logging.debug('Starting realtime transcription')
                        self.realtime_transcription_text = " ".join(
                            seg.text for seg in segments[0]
                        )
                        self.realtime_transcription_text = \
                            self.realtime_transcription_text.strip()

                        self.text_storage.append(
                            self.realtime_transcription_text
                            )

                        if len(self.text_storage) >= 2:
                            last_two_texts = self.text_storage[-2:]

                            prefix = os.path.commonprefix(
                                [last_two_texts[0], last_two_texts[1]]
                                )
                          
                            if len(prefix) >= \
                                    len(self.realtime_stabilized_safetext):

                                self.realtime_stabilized_safetext = prefix

                        matching_pos = self._find_tail_match_in_text(
                            self.realtime_stabilized_safetext,
                            self.realtime_transcription_text
                            )

                        if matching_pos < 0:
                            if self.realtime_stabilized_safetext:
                                self._on_realtime_transcription_stabilized(
                                    self._preprocess_output(
                                        self.realtime_stabilized_safetext,
                                        True
                                    )
                                )
                            else:
                                self._on_realtime_transcription_stabilized(
                                    self._preprocess_output(
                                        self.realtime_transcription_text,
                                        True
                                    )
                                )
                        else:
                            output_text = self.realtime_stabilized_safetext + \
                                self.realtime_transcription_text[matching_pos:]

                            self._on_realtime_transcription_stabilized(
                                self._preprocess_output(output_text, True)
                                )

                        self._on_realtime_transcription_update(
                            self._preprocess_output(
                                self.realtime_transcription_text,
                                True
                            )
                        )

                else:
                    time.sleep(TIME_SLEEP)

        except Exception as e:
            logging.error(f"Unhandled exeption in _realtime_worker: {e}")
            raise

    def _is_silero_speech(self, chunk):
        if self.sample_rate != 16000:
            pcm_data = np.frombuffer(chunk, dtype=np.int16)
            data_16000 = signal.resample_poly(
                pcm_data, 16000, self.sample_rate)
            chunk = data_16000.astype(np.int16).tobytes()

        self.silero_working = True
        audio_chunk = np.frombuffer(chunk, dtype=np.int16)
        audio_chunk = audio_chunk.astype(np.float32) / INT16_MAX_ABS_VALUE
        vad_prob = self.silero_vad_model(
            torch.from_numpy(audio_chunk),
            SAMPLE_RATE).item()
        is_silero_speech_active = vad_prob > (1 - self.silero_sensitivity)
        if is_silero_speech_active:
            self.is_silero_speech_active = True
        self.silero_working = False
        return is_silero_speech_active

    def _is_webrtc_speech(self, chunk, all_frames_must_be_true=False):
        if self.sample_rate != 16000:
            pcm_data = np.frombuffer(chunk, dtype=np.int16)
            data_16000 = signal.resample_poly(
                pcm_data, 16000, self.sample_rate)
            chunk = data_16000.astype(np.int16).tobytes()

        frame_length = int(16000 * 0.01)
        num_frames = int(len(chunk) / (2 * frame_length))
        speech_frames = 0

        for i in range(num_frames):
            start_byte = i * frame_length * 2
            end_byte = start_byte + frame_length * 2
            frame = chunk[start_byte:end_byte]
            if self.webrtc_vad_model.is_speech(frame, 16000):
                speech_frames += 1
                if not all_frames_must_be_true:
                    if self.debug_mode:
                        print(f"Speech detected in frame {i + 1}"
                              f" of {num_frames}")
                    return True
        if all_frames_must_be_true:
            if self.debug_mode and speech_frames == num_frames:
                print(f"Speech detected in {speech_frames} of "
                      f"{num_frames} frames")
            elif self.debug_mode:
                print(f"Speech not detected in all {num_frames} frames")
            return speech_frames == num_frames
        else:
            if self.debug_mode:
                print(f"Speech not detected in any of {num_frames} frames")
            return False

    def _check_voice_activity(self, data):
        self.is_webrtc_speech_active = self._is_webrtc_speech(data)
        if self.is_webrtc_speech_active:
            if not self.silero_working:
                self.silero_working = True
                threading.Thread(
                    target=self._is_silero_speech,
                    args=(data,)).start()

    def _is_voice_active(self):
        return self.is_webrtc_speech_active and self.is_silero_speech_active

    def _set_state(self, new_state):
        if new_state == self.state:
            return

        old_state = self.state

        self.state = new_state

        if old_state == "listening":
            if self.on_vad_detect_stop:
                self.on_vad_detect_stop()
        elif old_state == "wakeword":
            if self.on_wakeword_detection_end:
                self.on_wakeword_detection_end()

        if new_state == "listening":
            if self.on_vad_detect_start:
                self.on_vad_detect_start()
            self._set_spinner("speak now")
            if self.spinner and self.halo:
                self.halo._interval = 250
        elif new_state == "wakeword":
            if self.on_wakeword_detection_start:
                self.on_wakeword_detection_start()
            self._set_spinner(f"say {self.wake_words}")
            if self.spinner and self.halo:
                self.halo._interval = 500
        elif new_state == "transcribing":
            if self.on_transcription_start:
                self.on_transcription_start()
            self._set_spinner("transcribing")
            if self.spinner and self.halo:
                self.halo._interval = 50
        elif new_state == "recording":
            self._set_spinner("recording")
            if self.spinner and self.halo:
                self.halo._interval = 100
        elif new_state == "inactive":
            if self.spinner and self.halo:
                self.halo.stop()
                self.halo = None

    def _set_spinner(self, text):
        if self.spinner:
            if self.halo is None:
                self.halo = halo.Halo(text=text)
                self.halo.start()
            else:
                self.halo.text = text

    def _preprocess_output(self, text, preview=False):
        text = re.sub(r'\s+', ' ', text.strip())

        if self.ensure_sentence_starting_uppercase:
            if text:
                text = text[0].upper() + text[1:]

        if not preview:
            if self.ensure_sentence_ends_with_period:
                if text and text[-1].isalnum():
                    text += '.'

        return text

    def _find_tail_match_in_text(self, text1, text2, length_of_match=10):
        if len(text1) < length_of_match or len(text2) < length_of_match:
            return -1

        target_substring = text1[-length_of_match:]

        for i in range(len(text2) - length_of_match + 1):
            current_substring = text2[len(text2) - i - length_of_match:
                                      len(text2) - i]
            if current_substring == target_substring:
                return len(text2) - i

        return -1

    def _on_realtime_transcription_stabilized(self, text):
        if self.on_realtime_transcription_stabilized:
            if self.is_recording:
                self.on_realtime_transcription_stabilized(text)

    def _on_realtime_transcription_update(self, text):
        if self.on_realtime_transcription_update:
            if self.is_recording:
                self.on_realtime_transcription_update(text)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.shutdown()

    def transcribe_audio(self, audio_bytes):
        if isinstance(audio_bytes, bytes):
            audio_array = np.frombuffer(audio_bytes, dtype=np.int16)
            audio_array = audio_array.astype(np.float32) / INT16_MAX_ABS_VALUE
        else:
            audio_array = audio_bytes
        self.parent_transcription_pipe.send((audio_array, self.language))
        status, transcription = self.parent_transcription_pipe.recv()
        if status == 'success':
            return transcription
        else:
            raise Exception(transcription)