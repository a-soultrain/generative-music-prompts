"""
Setup script for the audio_brainstorm package.

This script uses setuptools to package the audio_brainstorm module, 
including its dependencies and metadata.
"""

from setuptools import setup, find_namespace_packages

setup(
    name='audio_brainstorm',  # The name of your package
    version='0.2.1',          # Version of your package
    packages=find_namespace_packages(  # Automatically find packages in the project
        include=['audio_brainstorm', 'audio_brainstorm.*']
    ),
    author='Enrique Garcia',
    author_email='jgarcia1312@gmail.com',
    description='A short description of your package',
    url='https://github.com/a-soultrain/generative_music_prompts',
)
