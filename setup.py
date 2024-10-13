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
    install_requires=[         # List your dependencies here
        'google-ai-generativelanguage==0.6.10',
        'google-api-core==2.20.0',
        'google-api-python-client==2.148.0',
        'google-auth==2.35.0',
        'google-auth-httplib2==0.2.0',
        'google-generativeai==0.8.3',
        'nltk==3.9.1',
        'python-dotenv==1.0.1',
        'requests==2.32.3',
        'joblib==1.4.2',
        'pydantic==2.9.2',
        'tqdm==4.66.5',
    ],
    author='Enrique Garcia',
    author_email='jgarcia1312@gmail.com',
    description='A short description of your package',
    url='https://github.com/a-soultrain/generative_music_prompts',
)
