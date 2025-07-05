# Start from an official Python base
FROM python:3.12-slim

# Create & use your app directory
WORKDIR /app

# Copy your code in
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Declare the default command
CMD ["python", "app/main.py"]
