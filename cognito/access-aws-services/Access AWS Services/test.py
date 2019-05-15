import boto3

client = boto3.client('sagemaker')

url = client.create_presigned_notebook_instance_url(
    NotebookInstanceName='NCADemo1',
    SessionExpirationDurationInSeconds=3600
)
print(url)
