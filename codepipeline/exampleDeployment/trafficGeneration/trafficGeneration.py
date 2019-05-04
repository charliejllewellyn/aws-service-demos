import boto3
import json
import random
import botocore.vendored.requests as requests
import uuid
import os
import time
from subprocess import Popen,PIPE,STDOUT
import re

inputbucket = os.environ['INPUT_BUCKET']
snsTopic = os.environ['SNS_TOPIC']
s3 = boto3.client('s3')

def getImageUrl():
    num = str(random.randint(1,101))
    r = s3.select_object_content(
            Bucket='cjl-temp-dub',
            Key='training_images/fall11_urls.txt',
            ExpressionType='SQL',
            Expression="select * from s3object s where s._1 like '%" + num + "%' limit 100",
            InputSerialization = {'CSV': {"FileHeaderInfo": "Ignore"}},
            OutputSerialization = {'JSON': {}},
    )
    return r

def getObject(url):
    return requests.get(url)
    
def checkValidImage(filename):
    out = Popen([ "file", '/tmp/' + filename ], stderr=STDOUT,stdout=PIPE)
    output = str(out.communicate()[0].decode("utf-8"))
    print(output)
    if re.search(".*JPEG.*", output):
        print('################ JPEG ############')
        return True
    else:
        print('################ NOT JPEG ############')
        return False

def uploadImage():
    for event in getImageUrl()['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            for line in records.splitlines():
                jsonData = json.loads(line)
                print(jsonData['_2'])
                try:
                    response = getObject(jsonData['_2'])
                    filename = str(uuid.uuid4()) + '.jpg'
                    open('/tmp/' + str(filename), 'wb').write(response.content)
                    if checkValidImage(filename):
                        s3.upload_file('/tmp/' + filename,inputbucket,filename,ExtraArgs={'ContentType': "image/jpeg"})
                        print('Uploaded file: ' + filename)
                        return
                    else:
                        continue
                except Exception as e:
                    print(e)
                    continue
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            
def sendSns():
    client = boto3.client('sns')
    response = client.publish(
    TopicArn=snsTopic,
    Message='trigger content'
)

def checktime(context):
    return context.get_remaining_time_in_millis()

def lambda_handler(event, context):
    while checktime(context) >= 15000:
        uploadImage()
        time.sleep(5)
    else:
        print('Starting new function')
        sendSns()
        return
