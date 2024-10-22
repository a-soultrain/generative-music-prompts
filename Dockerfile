FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./audio_brainstorm/ /app/audio_brainstorm/ 

EXPOSE 8000

CMD ["python", "-m", "audio_brainstorm.main"] 