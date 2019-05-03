import boto3
import json
import os

s3 = boto3.client('s3')

def getObjectDetails(event):
    bucket = event[1]['Records'][0]['s3']['bucket']['name']
    key = event[1]['Records'][0]['s3']['object']['key']
    return [ bucket, key ]

def readObject(event):
    s3Details = getObjectDetails(event)
    response = s3.get_object(
    Bucket=s3Details[0],
    Key=s3Details[1])
    return response['Body'].read().decode('utf-8')

def runComprehend(event):
    output = []
    textInput = readObject(event)
    response = comprehend.detect_sentiment(
        Text=textInput,
        LanguageCode='en'
    )
    output.append(response)
    response = comprehend.detect_entities(
        Text=textInput,
        LanguageCode='en'
    )
    output.append(response)
    response = comprehend.detect_key_phrases(
        Text=textInput,
        LanguageCode='en'
    )
    output.append(response)
    return output

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')
    print(event)
    event.append(runComprehend(event))
    return event
