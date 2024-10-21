# Use an appropriate Python base image (replace with your version if needed)
FROM python:3.12.7 

# Set the working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application listens on
EXPOSE 8000 

# Command to run your application
CMD ["python", "audio_brainstorm/main.py"]  # Update with your script path
