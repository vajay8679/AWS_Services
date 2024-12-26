import boto3
import os

# Initialize S3 client
s3_client = boto3.client('s3')

# Bucket name
bucket_name = 'local-ingest-bucket'

def upload_folder_to_s3(local_folder_path, bucket, s3_folder_prefix=''):
    """
    Upload a folder with multiple files to S3 bucket.
    :param local_folder_path: Local folder path containing files
    :param bucket: Target S3 bucket name
    :param s3_folder_prefix: Optional S3 folder prefix (path within the bucket)
    """
    try:
        for root, dirs, files in os.walk(local_folder_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                
                # Generate the S3 key (path inside bucket)
                relative_path = os.path.relpath(local_file_path, local_folder_path)
                s3_key = os.path.join(s3_folder_prefix, relative_path).replace("\\", "/")  # Use '/' for S3 paths
                
                # Upload file to S3
                s3_client.upload_file(local_file_path, bucket, s3_key)
                print(f"Uploaded: {local_file_path} to s3://{bucket}/{s3_key}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
local_folder = 'employee_data'  # Replace with your folder path
s3_folder_prefix = 'employee_data'       # Folder prefix in S3 (optional)

upload_folder_to_s3(local_folder, bucket_name, s3_folder_prefix)
