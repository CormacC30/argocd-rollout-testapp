FROM python:3.11-slim
WORKDIR /app
COPY error_app.py /app/error_app.py
RUN pip install Flask
EXPOSE 8080
CMD ["python3", "error_app.py"]