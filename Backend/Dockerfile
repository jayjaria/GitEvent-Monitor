# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .


# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "run.py"]
