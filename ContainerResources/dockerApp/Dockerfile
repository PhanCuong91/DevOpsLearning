# syntax=docker/dockerfile:1
FROM python:3.11-slim
WORKDIR /app
COPY app/ .
RUN python -m pip install flask
CMD ["python", "app.py"]
