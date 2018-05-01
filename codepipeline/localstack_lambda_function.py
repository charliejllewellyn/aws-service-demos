import boto3
import json

ipAddress = '172.17.0.3'

endpoint_url = 'http://' + ipAddress + ':4572'

s3 = boto3.client('s3', endpoint_url=endpoint_url)

def readHead(event):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.head_object(
    Bucket=bucket,
    Key=key)
    return response['ResponseMetadata']

def lambda_handler(event, context):
    print("It worked :)")
    print("The metadata for your object is...")
    return readHead(event)
