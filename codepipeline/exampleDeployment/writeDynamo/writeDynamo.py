import boto3
import os

def extractS3Info(event):
    s3Object = event[1]['Records'][0]['s3']['object']
    s3ObjectId = s3Object['eTag']
    s3ObjectKey = s3Object['key']
    s3ObjectType = event[0]['dataType']
    return s3ObjectId, s3ObjectKey, s3ObjectType

def addToDynamo(s3ObjectId, s3ObjectKey, s3ObjectType):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLENAME'])

    response = table.put_item(
        Item={
            'id': s3ObjectId,
            'Key': s3ObjectKey,
            'dataType': s3ObjectType,
        }
    )
    return response

def lambda_handler(event, context):
    s3ObjectDetails = extractS3Info(event)
    addToDynamo(s3ObjectDetails[0], s3ObjectDetails[1], s3ObjectDetails[2])
    return event
