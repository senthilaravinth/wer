FROM python:3.9-slim

WORKDIR /app

# Match your filename exactly
COPY fibnocci.py .

CMD ["python", "fibnocci.py"]