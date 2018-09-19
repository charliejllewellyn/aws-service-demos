import boto3
import json
import os

try:
    if os.environ['S3_ENDPOINT'] != '':
        endpoint_url = os.environ['S3_ENDPOINT']
    else:
        endpoint_url = None
except:
    endpoint_url = None

s3 = boto3.client('s3', endpoint_url=endpoint_url)

def getObjectDetails(event):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    return [ bucket, key ]

def readHead(event):
    s3Details = getObjectDetails(event)
    response = s3.head_object(
    Bucket=s3Details[0],
    Key=s3Details[1])
    return response['ResponseMetadata']['HTTPHeaders']['content-type']

def lambda_handler(event, context):
    # Comment in the below to demonstrate introducing a failure to rollback blue/green deployment
    #if readHead(event) == 'image/jpeg':
    #    event['Records'][0]['s3']['object']['key'] = 'non-existent-key'
    typeText = { 'dataType': readHead(event) }
    return typeText, event
