# Use a Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt requirements.txt

# Install dependencies (force cache update)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 5001

# Start the application
CMD ["python", "app.py"]
