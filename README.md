# AWS DRS Automation Using AWS Lambda
##  Restore EC2 instances via AWS DRS automatically using AWS Lambda



This automtion was created to automaticaly recover Ec2's or On-Prem VM's(which are registered in AWS DRS) to AWS . We have adehered best practices of Lambda + AWS DRS services. 


---
## Use Cases:
1. Automate recovery of applications hosted in Ec2 during an event of Disaster.
2. Perform DR drill of applcaitions.
---
## Prerequisites
1. AWS DRS agent installed and configured in your EC2 or VM,visit [Source server registrtion](https://docs.aws.amazon.com/drs/latest/userguide/agent-installation.html)
2. AWS DRS EC2 launch template configured,visit [DRS Launch Template](https://docs.aws.amazon.com/drs/latest/userguide/ec2-launch.html)
3. Recovery instance launch settings,visit [Ec2 Launch Settings](https://docs.aws.amazon.com/drs/latest/userguide/launching-target-servers.html)
---
# How It Works 
## Process Overview
1. This Repo uses CloudFormation template to launch the resources in AWS.Below are the services launched by CFT
      - AWS Lambda with Python 3.9 Runtime (Used to call AWS DRS API's) uses Boto3 
      - IAM Role required to restore servers using AWS DRS
2. Event to be passed to AWS Lambda:
      - For Point In Time Recovery (use Snapshot ID):
         ```
          {
              "IsDrill": "False",
              "SourceId": "s-xyzx1231sadasd231",
              "Snapshot_Id": "snap-0ewasd12342121o"
           }
           ```
      - Recover application servers from LATEST data (Don't pass any snapshot ID):
           ```
           {
              "IsDrill": "False",
              "SourceId": "s-xyzx1231sadasd231",
              "Snapshot_Id": ""
           }
           ``` 
---
 






