import json
import unittest
from writeDynamo.writeDynamo import extractS3Info
#import writeDynamo

s3EventMock = '''
[
  {
    "dataType": "text/plain"
  },
  {
    "Records": [
      {
        "eventVersion": "2.0",
        "eventSource": "aws:s3",
        "awsRegion": "eu-west-1",
        "eventTime": "2018-09-19T10:13:50.586Z",
        "eventName": "ObjectCreated:Put",
        "userIdentity": {
          "principalId": "AWS:AROAI4C7T3HZTNQDQJFL6:i-068de534a7eb59675"
        },
        "requestParameters": {
          "sourceIPAddress": "52.51.71.222"
        },
        "responseElements": {
          "x-amz-request-id": "7CC3A82B66228DF9",
          "x-amz-id-2": "fJAYD+QgVO14jOz34Zge+WS2c4iQtNnpSXsFLEWScXrKx/FtqbHxjvCK9EsVfz1qHkNwelsjhxA="
        },
        "s3": {
          "s3SchemaVersion": "1.0",
          "configurationId": "8c1455fa-d3f5-4a29-b839-f6275f022f6c",
          "bucket": {
            "name": "example-bucket",
            "ownerIdentity": {
              "principalId": "A7XKL26GUIEJO"
            },
            "arn": "arn:aws:s3:::codedeploy-demo-inputbucket-1o8fiqb6pw5wg"
          },
          "object": {
            "key": "test/key",
            "size": 2996,
            "eTag": "4401b86fe2f780d6ab13a56de66629d8",
            "sequencer": "005BA2215E89473DD2"
          }
        }
      }
    ]
  }
]
'''
 
class TestDataType(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_lambda_handler(self):
        self.assertEqual(extractS3Info(json.loads(s3EventMock)), ('4401b86fe2f780d6ab13a56de66629d8', 'test/key', 'text/plain'))
 
if __name__ == '__main__':
    unittest.main()
