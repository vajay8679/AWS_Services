# import boto3
# import os

# # Initialize S3 client
# s3_client = boto3.client('s3')

# # Bucket name
# bucket_name = 'local-ingest-bucket'

# def upload_file_to_s3(local_file_path, bucket, s3_key):
#     """
#     Upload a single file to S3.
#     """
#     try:
#         s3_client.upload_file(local_file_path, bucket, s3_key)
#         print(f"Uploaded file {local_file_path} to s3://{bucket}/{s3_key}")
#     except Exception as e:
#         print(f"Error uploading file {local_file_path}: {e}")


# # 1. Upload a single file
# local_file = 'employee.csv'
# upload_file_to_s3(local_file, bucket_name, 'employee.csv')



import boto3
import os

s3_client = boto3.client('s3')


def upload_to_s3(file_path,bucket,s3_key):
    try:
        s3_client.upload_file(file_path,bucket,s3_key)
        print(f"Uploaded file from {file_path} to s3://{bucket}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file {file_path}")


bucket_name = 'local-ingest-bucket'
file_path = 'employee.csv'

upload_to_s3(file_path,bucket_name,'employee.csv')



