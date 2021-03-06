import boto3
import json
import os

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')


def runRekognition(event):
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': event[1]['Records'][0]['s3']['bucket']['name'],
                'Name': event[1]['Records'][0]['s3']['object']['key'],
            }
        },
        MaxLabels=50,
    )
    return response

def lambda_handler(event, context):
    print(event[1]['Records'][0]['s3']['bucket']['name'])
    print(event[1]['Records'][0]['s3']['object']['key'])
    event[0]['ProcessingEngine'] = 'RekognitionImageDetectLabels'
    event.append(runRekognition(event))
    return event

