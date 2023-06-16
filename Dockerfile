FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cors_proxy.py .

ENV PORT 8080
CMD ["python", "cors_proxy.py"]