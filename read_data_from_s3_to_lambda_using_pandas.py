import boto3
import pandas as pd 
from io import BytesIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    print("event :",event)
    print("context :",context)
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_file_name = event["Records"][0]["s3"]["object"]["key"]
        print(bucket_name)
        print(s3_file_name)
        res = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
        print(res["Body"])
        df = pd.read_csv(res["Body"],sep=",")
        print(df)
    except Exception as err:
        print(err)