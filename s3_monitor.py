import boto3
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# AWS configuration
SOURCE_BUCKET = ""  # Source S3 bucket name
DESTINATION_BUCKET = ""  # Destination S3 bucket name
AWS_REGION = "us-east-1"  # Default AWS region

s3_client = boto3.client('s3', region_name=AWS_REGION)

def copy_object(key):
    """
    Copies an object from the source bucket to the destination bucket.
    """
    copy_source = {'Bucket': SOURCE_BUCKET, 'Key': key}
    try:
        s3_client.copy_object(CopySource=copy_source, Bucket=DESTINATION_BUCKET, Key=key)
        logger.info(f"Copied {key} from {SOURCE_BUCKET} to {DESTINATION_BUCKET}.")
    except Exception as e:
        logger.error(f"Error copying {key}: {e}")

def get_existing_keys():
    """
    Retrieves a list of all object keys currently in the source bucket.
    """
    try:
        response = s3_client.list_objects_v2(Bucket=SOURCE_BUCKET)
        if 'Contents' in response:
            return [item['Key'] for item in response['Contents']]
        else:
            return []
    except Exception as e:
        logger.error(f"Error listing objects in bucket {SOURCE_BUCKET}: {e}")
        return []

def main():
    logger.info(f"Starting S3 bucket monitor from {SOURCE_BUCKET} to {DESTINATION_BUCKET}.")

    existing_keys = set(get_existing_keys())

    while True:
        current_keys = set(get_existing_keys())
        new_keys = current_keys - existing_keys

        if new_keys:
            logger.info(f"Found {len(new_keys)} new object(s) in {SOURCE_BUCKET}.")
            for key in new_keys:
                copy_object(key)
            existing_keys = current_keys

        time.sleep(5)  # Wait for 10 seconds before checking again

if __name__ == "__main__":
    main()
