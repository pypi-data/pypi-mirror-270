from setuptools import setup, find_packages

setup(
    name = 'sapit',
    version = '1.5',
    description = 'A Text-to-speech module',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author_email = 'alilodhibusiness@gmail.com',
    author = 'Ali Lodhi',
    packages = ['sapit'],
    install_requires = [
        'pyttsx3 == 2.90',
        'pydub == 0.25.1',
        'ffmpeg == 1.4'
    ],

    entry_points = {
        "console_scripts": [
            "sapit = sapit:say",
        ],
    },
)