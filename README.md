# AWS DRS Automation Using AWS Lambda
##  Restore EC2 instances via AWS DRS automatically using AWS Lambda



This automtion was created to automaticaly recover Ec2's or On-Prem VM's(which are registered in AWS DRS) to AWS . We have adehered best practices of Lambda + AWS DRS services. 



## Use Cases:
1. Automate recovery of applications hosted in Ec2 during an event of Disaster at scale.
2. Perform DR drill of applcaitions at scale.

## Prerequisites
1. AWS DRS agent installed and configured in your EC2 or VM. [Source server registrtion](https://docs.aws.amazon.com/drs/latest/userguide/agent-installation.html)
2. AWS DRS EC2 launch template configured. [DRS Launch Template](https://docs.aws.amazon.com/drs/latest/userguide/ec2-launch.html)
3. Recovery instance launch settings. [Ec2 Launch Settings](https://docs.aws.amazon.com/drs/latest/userguide/launching-target-servers.html)

## Process Overview








AWS Services Used
AWS DRS - Elastic Disaster Recovery Service
AWS Lambda
AWS CloudFomation 
