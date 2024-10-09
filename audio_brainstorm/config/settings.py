"""
This module handles configuration and setup for the audio_brainstorm project.

It includes:
- Loading environment variables
- Setting up logging
- Initializing the Google Generative AI library
"""
import logging
import os
from dotenv import load_dotenv

import google.generativeai as palm

# Load variables from .env file
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError(
        "No API Key found. Please set the GOOGLE_API_KEY environment variable")

palm.configure(api_key=api_key)

# Configure logging
logging.basicConfig(
    filename='audio_brainstorm.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
