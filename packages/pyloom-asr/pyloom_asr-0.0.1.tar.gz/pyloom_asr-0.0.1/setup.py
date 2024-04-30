from setuptools import setup, find_packages

setup(
    name='pyloom_asr',
    version='0.0.1',
    packages=find_packages(),
    description='Advanced real-time voice processing library using Whisper and Silero models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dibyaprakash',
    author_email='dibyapp@outlook.com',
    url='https://github.com/dibyapp/pyloom-asr',
    license='MIT',
    install_requires=[
        'torch',
        'scipy',
        'faster-whisper',
        'pvporcupine',
        'webrtcvad',
        'pyaudio',
        'halo',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
