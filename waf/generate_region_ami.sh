for region in $(cat ~/.aws/regions.txt); do
	amiId=$(aws ec2 describe-images --owners amazon --region $region  --filter "Name=description,Values=Amazon Linux AMI 2018*x86_64 HVM GP2" | jq -c '.Images[] | {ImageId}' | tail -1 | awk -F\" '{print $4}')
	echo -e "${region}\n  \"64\": \"$amiId\""
done

#aws ec2 describe-images --owners amazon   --filter "Name=description,Values=Amazon Linux AMI 2018*x86_64 HVM GP2" | jq -c '.Images[] | {ImageId}' | tail -1 | awk -F\" '{print $4}'
