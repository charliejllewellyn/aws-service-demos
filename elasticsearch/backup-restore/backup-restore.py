import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://search-sauron-qlz4lu3si5bctffiknha7gmnhm.eu-west-1.es.amazonaws.com/' # include https:// and trailing /
region = 'eu-west-1' # e.g. us-west-1
service = 'es'
reponame = '' # e.g. my-repo
bucketname = 'cjl-eu-west-2' # do NOT include s3:// or trailing / e.g. sample-bucket-name
prefix = '/sample_datasets/enron_emails/elasticsearch_backup' # include starting / but do NOT include trailing / e.g. /elasticsearch_backup
backupRoleArn = 'arn:aws:iam::008369042577:role/elasticsearch-backup-role' # IAM role with trust for ES to access the bucket, see https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html, e.g. arn:aws:iam::111111111111:role/elasticsearch-backup-role
snapshotname = '' # e.g. mysnapshot

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository

def setupRepo():
  path = '_snapshot/' + reponame # the Elasticsearch API endpoint
  url = host + path
  
  payload = {
    "type": "s3",
    "settings": {
      "bucket": bucketname,
      "base_path": prefix,
      "region": region,
      "role_arn": backupRoleArn
    }
  }
  
  headers = {"Content-Type": "application/json"}
  
  r = requests.put(url, auth=awsauth, json=payload, headers=headers)
  
  print(r.status_code)
  print(r.text)

def listRepos():
  path = '_snapshot/cs-automated/_all?pretty' # the Elasticsearch API endpoint
  #path = '_snapshot' # the Elasticsearch API endpoint
  url = host + path

  headers = {"Content-Type": "application/json"}

  r = requests.get(url, auth=awsauth, headers=headers)

  print(r.status_code)
  print(r.text)

# Take snapshot

def takeSnapshot():
  path = '_snapshot/' + reponame + '/' + snapshotname
  url = host + path
 
  r = requests.put(url, auth=awsauth)
 
  print(r.text)

# Get snapshot status

def getSnapshotStatus():
  path = '_snapshot/' + reponame + '/' + snapshotname
  url = host + path

  r = requests.get(url, auth=awsauth)

  print(r.text)

# Delete index

def deleteIndex():
  #path = '.kibana_1'
  path = 'sauron-2019-w27'
  url = host + path
 
  r = requests.delete(url, auth=awsauth)
 
  print(r.text)
 
# Restore snapshots (all indices)

def restoreAllIndicies():
  path = '_snapshot/' + reponame + '/' + snapshotname + '/_restore'
  url = host + path
 
  r = requests.post(url, auth=awsauth)
 
  print(r.text)

# Restore snapshot (one index)

def restoreSingleIndex():
  path = '_snapshot/' + reponame + '/' + snapshotname + '/_restore'
  url = host + path
  
  payload = {"indices": "enronemails"}
  
  headers = {"Content-Type": "application/json"}
  
  r = requests.post(url, auth=awsauth, json=payload, headers=headers)
  
  print(r.text)

def createIndex():
  path = 'test'
  url = host + path

  headers = {"Content-Type": "application/json"}

  r = requests.put(url, auth=awsauth, headers=headers)

  print(r.text)

def insertData():
  path = 'test/test'
  url = host + path

  payload = {"request": {"data": "Test message from somewhere!"}, "id": "req_123"}

  headers = {"Content-Type": "application/json"}

  r = requests.post(url, auth=awsauth, json=payload, headers=headers)

  print(r.text)

#createIndex()
#insertData()
#setupRepo()
#listRepos()
#getSnapshotStatus()
deleteIndex()
#restoreAllIndicies()
#restoreSingleIndex()
