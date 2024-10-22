"""
This module handles configuration and setup for the audio_brainstorm project.

It includes:
- Loading environment variables
- Setting up logging
- Initializing the Google Generative AI library
"""
import logging

# Configure logging
logging.basicConfig(
    filename='audio_brainstorm.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
