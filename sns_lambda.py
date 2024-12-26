# sending message to mail without publishing message if we are using lambda
import boto3
import pandas as pd 
from io import BytesIO

client = boto3.client('sns')
snsArn = 'arn:aws:sns:ap-south-1:772943381465:sns-test-tpoic'

def lambda_handler(event, context):
    # TODO implement
    message = 'This is SNS service for s3 files'
    response = client.publish(
        TargetArn = snsArn,
        Message = message,
        MessageStructure = 'text'
    )

    print(response)
    


