import boto3
import json
import os

comprehend = boto3.client('comprehend')


def getText(event):
    words = []
    for text in event[2]['TextDetections']:
        words.append(text['DetectedText'])
    return ' '.join(map(str,words))

def runComprehend(event):
    output = []
    textInput = getText(event)
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
    event[0]['ProcessingEngine'] = 'RekognitionImageComprehend'
    event.append(runComprehend(event))
    return event
