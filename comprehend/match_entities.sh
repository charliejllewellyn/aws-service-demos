aws comprehend start-entities-detection-job \
     --entity-recognizer-arn "arn:aws:comprehend:eu-west-1:008369042577:entity-recognizer/street-drug-entities" \
     --job-name 'drugTest' \
     --data-access-role-arn "arn:aws:iam::008369042577:role/service-role/AmazonComprehendServiceRoleS3FullAccess-comprehend_s3" \
     --language-code en \
     --input-data-config "S3Uri=s3://cjl-temp-dub/comprehend/" \
     --output-data-config "S3Uri=s3://cjl-temp-dub/" \
     --region eu-west-1
