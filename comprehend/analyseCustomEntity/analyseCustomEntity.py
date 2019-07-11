import boto3
import json
import os

#s3 = boto3.client('s3', endpoint_url=endpoint_url)

def getEventDetails(event):

    matched_entities = []
    for entity in event['Entities']:
        if entity['Score'] > 0.5:
            matched_entities.append(entity)
    return matched_entities

def lambda_handler(event, context):
    return getEventDetails(event)
