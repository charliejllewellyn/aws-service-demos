import boto3
import json
import os

s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')


def getObjectDetails(event):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    return [ bucket, key ]

def readObject(event):
    s3Details = getObjectDetails(event)
    response = s3.get_object(
    Bucket=s3Details[0],
    Key=s3Details[1])
    return response['Body'].read().decode('utf-8')

def runComprehend(event):
    response = comprehend.detect_sentiment(
        Text=readObject(event),
        LanguageCode='en'
    )
    return response

def lambda_handler(event, context):
    print(event)
    event.append(runComprehend(event))
    return event
