from setuptools import setup, find_packages

setup(
    name='praanscribe',
    version='1.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'praanscribe=praanscribe.py:main',
        ],
    },
    install_requires=[
        'SpeechRecognition',
        # Add other dependencies if needed
    ],
    author='Ali Çağan Kaya',
    author_email='alicagank@icloud.com',
    description='A small application for automatically transcribing audio and creating TextGrid files to be used in Praat.',
    url='https://github.com/alicagank/praanscribe',
)
