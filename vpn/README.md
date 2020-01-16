# Overview
This template deploys a simple non-HA, VPN tunnel to replicate an on-premesis VPN solution connecting to an AWS VPC.

<p align="center">
  <img width="900" src="https://github.com/charliejllewellyn/aws-service-demos/blob/master/vpn/images/Static_VPN.png">
</p>

## Pre-reqs

To deploy this stack you need to provide a keypair. If you have not already created one follow this guide, 
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html.
# Deployment

To deploy the stack click on the buttons below.

| Region| Region Code | Launch |
|------|:------:|-------:|
| EU West 2 (London)| <span style="font-family:'Courier';">eu-west-2</span> | [![Launch Step 0A in eu-west-2](images/cfn-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=VPN&templateURL=https://cjl-eu-west-2.s3.eu-west-2.amazonaws.com/cloudformation-templates/aws-service-demos/vpn/vpn-static.template) |
| EU West 1 (Ireland)| <span style="font-family:'Courier';">eu-west-1</span> | [![Launch Step 0A in eu-west-1](images/cfn-launch-stack.png)](https://cjl-eu-west-1.s3.eu-west-2.amazonaws.com/cloudformation-templates/aws-service-demos/vpn/vpn-static.template) |

## Testing

To test the deployment head over to the EC2 console and get the public hostname of the instance named "Onprem-VPN-Instance". SSH to the instance and run a ping from the server to the private IP of the instance "AWS-Test-Instance".  
