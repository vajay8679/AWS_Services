import requests
import boto3

s3_client = boto3.client('s3')

def upload_from_url(url,bucket,s3_key):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        s3_client.upload_fileobj(response.raw, bucket,s3_key)
        print(f"file uploaded successfully from {url}")
    except Exception as e:
        print(f"Error while uploading {url} : {e}")

# url = "https://www.kaggle.com/datasets/teseract/urldataset?select=urldata.csv"
url = "https://raw.githubusercontent.com/vajay8679/PySpark/refs/heads/main/PySpark_Practical/flight_data.csv"
bucket_name = 'local-ingest-bucket'
s3_key = 'url_folder/flight_data.csv'

upload_from_url(url,bucket_name,s3_key)