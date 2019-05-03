import boto3
import json
import os

s3 = boto3.client('s3')

def writeObject(event):
    bucket = os.environ['OUTPUT_BUCKET']
    key = event[0]['ProcessingEngine'] + '/' + event[1]['Records'][0]['s3']['object']['key']
    data = event[2]
    data['ObjectId'] = key
    fileData = str.encode(json.dumps(data))
    response = s3.put_object(
    Bucket=bucket,
    Key=key,
    Body=fileData)
    return response

def lambda_handler(event, context):
    for singleEvent in event:
      print(writeObject(singleEvent))
    return 



