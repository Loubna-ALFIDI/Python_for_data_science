FROM python:3.12-alpine

WORKDIR /app

COPY test.py .

CMD ["python3", "test.py"]
