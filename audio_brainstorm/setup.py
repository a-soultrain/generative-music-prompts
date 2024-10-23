"""
Setup script for the audio_brainstorm package.

This script uses setuptools to package the audio_brainstorm module, 
including its dependencies and metadata.
"""

from setuptools import setup, find_namespace_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    required = f.read().splitlines()

setup(
    name='audio_brainstorm',
    version='0.2.1',
    packages=find_namespace_packages(
        include=['audio_brainstorm', 'audio_brainstorm.*']
    ),
    author='Enrique Garcia',
    author_email='jgarcia1312@gmail.com',
    description='A short description of your package',
    url='https://github.com/a-soultrain/generative_music_prompts',
    install_requires=required,
)
