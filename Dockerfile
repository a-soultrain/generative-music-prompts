FROM python:3.12.7-slim-bullseye

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y git

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 

CMD ["python3", "audio_brainstorm/main.py"]