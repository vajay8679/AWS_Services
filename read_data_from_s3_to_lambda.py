import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    print("event :",event)
    print("context :",context)
    print("Hello this is my first function !!!")
    
    bucket = s3.Bucket("local-ingest-bucket")
    print(bucket.objects.all())

    for obj in bucket.objects.all():
        key = obj.key
        print(key)