import boto3
import json
import os

s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')

def readObject(event):
    bucket = event[1]['Records'][0]['s3']['bucket']['name']
    key = event[1]['Records'][0]['s3']['object']['key']
    response = s3.get_object(
    Bucket=bucket,
    Key=key)
    return response['Body'].read().decode('utf-8')

def runComprehend(event):
    response = comprehend.detect_sentiment(
        Text=readObject(event),
        LanguageCode='en'
    )
    return response

def lambda_handler(event, context):
    print(event)
    print(runComprehend(event))
    return 
