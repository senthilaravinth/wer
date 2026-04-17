FROM python:3.9-slim

WORKDIR /app

# Copy the script into the container
COPY fibonacci.py .

# Run the script when the container starts
CMD ["python", "fibonacci.py"]