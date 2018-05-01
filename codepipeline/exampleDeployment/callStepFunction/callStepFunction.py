import boto3
import json
import uuid

client = boto3.client('stepfunctions')
print(uuid.uuid4())

def invokeStepFunction(event):
    for stateMachine in client.list_state_machines()['stateMachines']:
        if stateMachine['name'] == 'Demo-state-machine':
            stateMachineArn = stateMachine['stateMachineArn']
    response = client.start_execution(
        stateMachineArn=stateMachineArn,
        name=str(uuid.uuid4()),
        input=json.dumps(event))
    return response

def lambda_handler(event, context):
    invokeStepFunction(event)
    return 
