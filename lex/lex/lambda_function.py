import boto3
import json
print('9')

def getDynamoData(event):
    dynamoDBTable = 'lexDemo'
    emailAddress = event['currentIntent']['slots']['emailAddress']

    client = boto3.client('dynamodb')

    response = client.query(
        ExpressionAttributeValues={
            ':v1': {
                'S': emailAddress.lower(),
            },
        },
        KeyConditionExpression='userEmail = :v1',
        TableName=dynamoDBTable,
    )
    print(response)
    return response['Items'][0]['Type']['M']['firearmsApplication']['S']

def complete(event):
    response = {
      "dialogAction": {
        "type": "ElicitSlot",
        "message": {
          "contentType": "PlainText",
          "content": "Your application status has been updated as: " + getDynamoData(event) + ". Thank you for your call, goodbye."
        },
       "intentName": "callDescription",
       "slots": {
          "callDescriptionSlot": event['currentIntent']['slots']['callDescriptionSlot'],
          "emailAddress": event['currentIntent']['slots']['emailAddress'],
          "passwordOne": event['currentIntent']['slots']['passwordOne'],
          "passwordTwo": event['currentIntent']['slots']['passwordTwo']
       },
       "slotToElicit" : "emailAddress"
      }
    }
    return response

def build_response(event):
    response = {
      "dialogAction": {
        "type": "ElicitSlot",
        "message": {
          "contentType": "PlainText",
          "content": "okay, we just need to validate who you are, please can I have your username?"
        },
       "intentName": "callDescription",
       "slots": {
          "callDescriptionSlot": event['currentIntent']['slots']['callDescriptionSlot'],
          "emailAddress": None,
          "passwordOne": None,
          "passwordTwo": None,
       },
       "slotToElicit" : "emailAddress"
      }
    }
    return response

def build_passwordOne_response(event):
    response = {
      "dialogAction": {
        "type": "ElicitSlot",
        "message": {
          "contentType": "PlainText",
          "content": "okay, what is the first number in your pin?"
        },
       "intentName": "callDescription",
       "slots": {
          "callDescriptionSlot": event['currentIntent']['slots']['callDescriptionSlot'],
          "emailAddress": event['currentIntent']['slots']['emailAddress'],
          "passwordOne": None,
          "passwordTwo": None,
       },
       "slotToElicit" : "passwordOne"
      }
    }
    return response
    
def build_agent_response(event):
    response = {
      "dialogAction": {
        "type": "close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText",
          "content": "okay, transferring you to caller?"
        },
       "intentName": "ConnectToAgent",
       "slots": {}
      }
    }
    return response
    
def build_passwordTwo_response(event):
    response = {
      "dialogAction": {
        "type": "ElicitSlot",
        "message": {
          "contentType": "PlainText",
          "content": "okay, what is the fith number in your pin?"
        },
       "intentName": "callDescription",
       "slots": {
          "callDescriptionSlot": event['currentIntent']['slots']['callDescriptionSlot'],
          "emailAddress": event['currentIntent']['slots']['emailAddress'],
          "passwordOne": event['currentIntent']['slots']['passwordOne'],
          "passwordTwo": None
       },
       "slotToElicit" : "passwordTwo"
      }
    }
    return response

def lambda_handler(event, context):
    print(event)
    if 'ConnectToAgent' == event['currentIntent']['name']:
        print(build_agent_response(event))
        return build_agent_response(event)
    else:
        if event['currentIntent']['slots']['emailAddress'] == None:
            print(build_response(event))
            return build_response(event)
        elif event['currentIntent']['slots']['passwordOne'] == None:
            return build_passwordOne_response(event)
        elif event['currentIntent']['slots']['passwordTwo'] == None:
            return build_passwordTwo_response(event)
        else:
            return complete(event)
