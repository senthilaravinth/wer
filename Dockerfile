FROM python:3.9-slim

# Set workspace
WORKDIR /app

# Copy the file from your computer into the container image
# The '.' means "the current directory"
COPY fibnocci.py .

# Execute the script
CMD ["python", "fibnocci.py"]