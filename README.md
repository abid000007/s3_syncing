# S3 Bucket Monitor & Sync

This repository contains a Dockerized Python script designed to monitor an AWS S3 bucket and automatically sync its contents with another S3 bucket. The solution is ideal for ensuring that two S3 buckets stay synchronized without manual intervention.

## Features

- **Automated Monitoring**: Continuously monitors a source S3 bucket for any changes.
- **Bucket Synchronization**: Automatically syncs changes from the source bucket to the destination bucket.
- **Dockerized Deployment**: The entire solution is containerized using Docker for easy deployment and management.
- **AWS Integration**: Utilizes Boto3 for seamless integration with AWS S3 services.

## Prerequisites

- Docker installed on your local machine or server.
- AWS credentials with appropriate permissions to access and modify the S3 buckets.
- Python 3.x (if running the script locally outside of Docker).

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abid000007/s3_syncing.git
    cd s3_syncing
    ```

2. **Build the Docker image**:
    ```bash
    docker build -t s3-bucket-monitor-sync .
    ```

3. **Run the Docker container**:
    ```bash
    docker run -e AWS_ACCESS_KEY_ID=your_access_key_id \
               -e AWS_SECRET_ACCESS_KEY=your_secret_access_key \
               -e SOURCE_BUCKET=your_source_bucket_name \
               -e DESTINATION_BUCKET=your_destination_bucket_name \
               s3-bucket-monitor-sync
    ```

4. **Environment Variables**:
    - `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
    - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
    - `SOURCE_BUCKET`: The name of the S3 bucket to monitor.
    - `DESTINATION_BUCKET`: The name of the S3 bucket to sync changes to.

## Configuration

The script can be customized by modifying the Python code in `sync.py`. You can adjust the polling interval, error handling, and logging as per your requirements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute to this project.

---

You can find the repository at: [https://github.com/abid000007/s3_syncing/](https://github.com/abid000007/s3_syncing/)
