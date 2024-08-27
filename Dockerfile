FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files and to ensure stdout/stderr are unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set AWS credentials and region environment variables
ENV AWS_ACCESS_KEY_ID=#add access id
ENV AWS_SECRET_ACCESS_KEY= #add access key
ENV AWS_REGION=eu-north-1

# Install necessary system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
#COPY requirements.txt /app/
RUN pip install boto3

# Copy the Python script into the container
COPY s3_monitor.py /app/

# Command to run the Python script
CMD ["python3", "s3_monitor.py"]
