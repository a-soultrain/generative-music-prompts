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
    install_requires=[
        'annotated-types==0.7.0',
        'astroid==3.3.5',
        'cachetools==5.5.0',
        'certifi==2024.8.30',
        'charset-normalizer==3.3.2',
        'click==8.1.7',
        'dill==0.3.9',
        'docstring_parser==0.16',
        'httplib2==0.22.0',
        'idna==3.10',
        'isort==5.13.2',
        'joblib==1.4.2',
        'mccabe==0.7.0',
        'mido==1.3.2',
        'numpy==2.1.2',
        'packaging==23.2',
        'platformdirs==4.3.6',
        'pretty_midi==0.2.10',
        'proto-plus==1.24.0',
        'protobuf==5.28.2',
        'pyasn1==0.6.1',
        'pyasn1_modules==0.4.1',
        'pydantic==2.9.2',
        'pydantic_core==2.23.4',
        'pylint==3.3.1',
        'pyparsing==3.1.4',
        'python-dateutil==2.9.0.post0',
        'python-dotenv==1.0.1',
        'regex==2024.9.11',
        'requests==2.32.3',
        'rsa==4.9',
        'shapely==2.0.6',
        'six==1.16.0',
        'tomlkit==0.13.2',
        'tqdm==4.66.5',
        'typing_extensions==4.12.2',
        'uritemplate==4.1.1',
        'urllib3==2.2.3'
    ]
)
