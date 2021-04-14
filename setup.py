from setuptools import setup

with open('DESCRIPTION.txt') as file:
    long_description = file.read()


REQUIREMENTS =['chat_downloader', 'click']

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Streamers',
    'Topic :: YouTube',
    'License :: MIT License',
    'Programming Language :: Python'
]

setup(
    name='ladyredhood-chats',
    version='0.1.0',
    description='A small script to extract timestamps from youtube chats',
    long_description=long_description,
    author='Aurghyadip Kundu',
    author_email='director@webedutech.org',
    license='MIT',
    packages=['chats'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords='youtube youtube-chat youtube-timestamp'
)