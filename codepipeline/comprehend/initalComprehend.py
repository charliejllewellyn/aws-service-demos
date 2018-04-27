import boto3
import json

comprehend = boto3.client('comprehend')
s3 = boto3.client('s3')

def readObject(event):
    response = s3.get_object(
    Bucket=event['bucket'],
    Key=event['key'])
    return response['Body'].read().decode("utf-8")

def comprehendDetectSentiment(text):
    response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    return(response['Sentiment'])

def lambda_handler(event, context):
    text = readObject(event)
    return {"sentiment": comprehendDetectSentiment(text)}
