# Zip layer and upload
zip -r python_libs.zip ./python
aws lambda publish-layer-version --layer-name lambdaLayerDemo --zip-file fileb://python_libs.zip --compatible-runtimes python3.7

# Create new function
Create new Lambda function with runtim python3.7
Add layer
Add code
```
import custom_func as cf

def lambda_handler(event, context):
    cf.cust_fun()
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda Layers!'
    }
```
