FROM python:3.11-slim
WORKDIR /app
COPY error_app.py /app/error_app.py
RUN pip install Flask && pip install prometheus_client
EXPOSE 8080
CMD ["python3", "error_app.py"]