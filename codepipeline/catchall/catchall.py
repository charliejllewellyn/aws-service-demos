import subprocess as sub
import boto3
import os

def getObj():
    os.chdir('/tmp')
    s3 = boto3.resource('s3')
    s3.meta.client.download_file('cjl-chelt-hack', 'masterbuilder.jpg', 'masterbuilder.jpg')
    p = sub.Popen(['file', 'masterbuilder.jpg'],stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    print(output)

def lambda_handler(event, context):
    print(event)
    # TODO implement
    return 'Complete'
