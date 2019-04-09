# Overview

This example pattern will show you how to run Glue ETL jobs to read data from S3 and push to Kinesis Firehose and then out to Elasticsearch

This template with deploy:

An input S3 bucket to store files to ingest
An output S3 bucket to store and records that fail to push to Elasticsearch
AWS Elasticsearch as a public cluster
A kinesis firehose data stream
A Glue job with a smaple script to read a parquet file and psuh the records to Kinesis Firehose which pushes them to Elasticsearch
A Cognito UserPool for Elasticsearch

# Setup

To Setup deploy the template setupPipeline.yaml

e.g.

```
aws cloudformation create-stack --stack-name glueKinesisEsDemo --template-body file://setupPipeline.yaml --region eu-west-2 --capabilities CAPABILITY_IAM
```

# Post config

Cloudformation does not yet fully support Cognito or Elasticsearch. Therefore if you want to enable Coginto integration with Elasticsearch you need to peform the following steps:

1. Add a domain to the Cognito UserPool
Follow this guide to enable it https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html. The userpool name is *KibanaUsers*

2. Update the Elasticsearch cluster to use Cognito
- In the AWS service console select Elasticsearch and then select the ES domain that was created
- Click configure cluster and check "Enable Amazon Cognito for authentication"
- Select *KibanaUsers* for "Cognito User Pool"
- Select KibanaIDPool for "Cognito Identity Pool"
- Enter *CognitoAccessForAmazonES* for "IAM Role Name"
- Click submit changes
