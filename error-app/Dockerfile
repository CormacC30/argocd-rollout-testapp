FROM python:3.11-slim
WORKDIR /app
COPY logging.py /app/logging.py
RUN pip install Flask
EXPOSE 8080
CMD ["python", "logging.py"]