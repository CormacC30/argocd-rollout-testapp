FROM python:3.9-slim
WORKDIR /app
COPY healthy-app.py /app/healthy-app.py
RUN pip install flask
EXPOSE 8080
CMD ["python", "healthy_app.py"]