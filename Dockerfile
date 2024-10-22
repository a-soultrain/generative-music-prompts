FROM python:3.12.7-slim-bullseye

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

COPY ./audio_brainstorm /app

EXPOSE 8000 

CMD ["python3", "main.py"]