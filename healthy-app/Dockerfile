FROM python:3.11-slim
WORKDIR /app
COPY healthy-app.py /app/healthy-app.py
RUN pip install flask
EXPOSE 8080
CMD ["python3", "healthy-app.py"]