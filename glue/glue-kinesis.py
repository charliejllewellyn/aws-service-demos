import boto3
import io
import pandas as pd
import os
import sys
import re
import os
from subprocess import Popen,PIPE,STDOUT
import sys
from datetime import datetime

# Install some extra modules for pandas and to handle datetime serialisation in json
out = Popen(["pip", "install", "pyarrow", "-t", "./", "--cache-dir=/tmp/"], stderr=STDOUT,stdout=PIPE)
print(out.communicate()[0])
out2 = Popen(["pip", "install", "jsonplus", "-t", "./", "--cache-dir=/tmp/"], stderr=STDOUT,stdout=PIPE)
print(out2.communicate()[0])
import jsonplus as json

# Read the parquet file
buffer = io.BytesIO()
s3 = boto3.resource('s3')
object = s3.Object('gluekinesisesdemo-outputbucket-1q02gbafj0egc','part-00000-985a5178-964e-43e1-8087-b5ca12ac2604-c000.snappy.parquet')
object.download_fileobj(buffer)
df = pd.read_parquet(buffer)

#Create iterator to batch
def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

# Send data to Firehose
client = boto3.client('firehose')
def doc_generator(df):
    for batchRecord in batch(df, 499):
        df_iter = batchRecord.iterrows()
        for index, document in df_iter:
            recordset = []
            recordset.append({'Data': bytes(json.dumps({'gender': document['gender'],'emp_no': document['emp_no'], 'birth_date': document['birth_date'], 'last_name': document['last_name'], 'hire_date': document['hire_date'], 'first_name': document['first_name']}))})
            response = client.put_record_batch(
                DeliveryStreamName='glueKinesisEsDemo-ElasticSearchDeliveryStream-KDNUH7D8KJZG',
                Records=recordset
            )
            print(response)
    
print(doc_generator(df))
