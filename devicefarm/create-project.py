import boto3
import json
from bson import json_util
import requests

client = boto3.client('devicefarm', region_name='us-west-2')
apkDownloadUrl='https://download.apkpure.com/b/apk/Y29tLmFtYXpvbi5hd3MuY29uc29sZS5tb2JpbGVfMTkwNTAwMDAxMF9jNjEzMmQyYw?_fn=QVdTIENvbnNvbGVfdjEuMTkuNV9hcGtwdXJlLmNvbS5hcGs&k=76a6db5cfc97fb7b14c35f302a2449fd5afec47f&as=fa5514449cfa2befe78cbb604fa8af065afc21f7&_p=Y29tLmFtYXpvbi5hd3MuY29uc29sZS5tb2JpbGU&c=1%7CBUSINESS%7CZGV2PUFXUyUyME1vYmlsZSUyMExMQyZ2bj0xLjE5LjUmdmM9MTkwNTAwMDAxMA'

def downloadApk():
    r = requests.get(apkDownloadUrl)
    open('Console_v1.19.5_apkpure.com.apk', 'wb').write(r.content)

def createProject():
    response = client.create_project(
        name='chris-demo',
        defaultJobTimeoutMinutes=123
    )
    return response['project']['arn']

def uploadApk(projectArn):
    response = client.create_upload(
        name='Console_v1.19.5_apkpure.com.apk',
        type='ANDROID_APP',
        projectArn=projectArn,
    )
    url = response['upload']['url']
    
    data = open('Console_v1.19.5_apkpure.com.apk','rb').read()
    headers = {'Content-Type': 'application/octet-stream'}
    r = requests.put(url, data=data, headers=headers)
    return response['upload']['arn']

def getUploadDetails(uploadArn):
    response = client.get_upload(
        arn=uploadArn,
    )
    print('Upload details\n')
    print(json.dumps(response, indent=4, sort_keys=True, default=json_util.default))

print('Downloading AWS console Android app APK...')
downloadApk()
print('Download complete')
print('Create new devicefarm project...')
projectArn = createProject()
print('Project created')
print('Uploading Android APK to devicefarm...')
uploadArn = uploadApk(projectArn)
print('Upload complete')
print(uploadArn)
getUploadDetails(uploadArn)
