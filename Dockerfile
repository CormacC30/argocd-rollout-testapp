FROM python:3.9-slim
WORKDIR /app
COPY logging.py /app/app.py
RUN pip install Flask
EXPOSE 8080
CMD ["python", "app.py"]