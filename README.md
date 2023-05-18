# AWS DRS Automation Using AWS Lambda
##  Restore EC2 instances via AWS DRS automatically using AWS Lambda


  <img src = "https://github.com/vidyashankar13/aws-drs-automation/assets/50440333/68b3c9a2-4dd9-468b-9a0c-8ae534d36a09" width=750 height=500>


This utility is to automatize recovery of EC2's or On-Prem VM's(which are registered in AWS DRS) to AWS . We have adhered to best practices of AWS Lambda + AWS DRS services. 

---
## Use Cases:
1. Automate recovery of applications hosted in Ec2 during an event of disaster. (Recovery can be Point-In-time or Latest)
2. Perform DR drills of applications
---
## Prerequisites
1. AWS DRS agent installed and configured in your EC2 or VM,visit [Source server registrtion](https://docs.aws.amazon.com/drs/latest/userguide/agent-installation.html)
2. AWS DRS EC2 launch template configured,visit [DRS Launch Template](https://docs.aws.amazon.com/drs/latest/userguide/ec2-launch.html)
3. Recovery instance launch settings,visit [Ec2 Launch Settings](https://docs.aws.amazon.com/drs/latest/userguide/launching-target-servers.html)
4. S3 bucket 
---

##  Overview
1. This repository uses CloudFormation template to launch the resources in AWS.Below are the services launched by CFT
      - AWS Lambda with Python 3.9 Runtime.
      - IAM Role with IAM policy required to restore servers using AWS DRS
2. Lambda function uses Boto3 to make AWS DRS API calls to perform recovery opertaions.
 # How To Guide:
  1. Upload drs-repl.zip to an S3 bucket and note the path
  2. Create a CloudFormation Stack using the lambda.yaml template
  3. Event to be passed to AWS Lambda:
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
  4. You can invocate your lambda in multiple ways, visit [Invoking Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html)
---
## Parmeters used in CFT
1. pLambdaFnName - Valid name of the Lambda function
2. pBucketName - S3 bucket name where lambda deployment (.zip) file is uploaded
3. pZipFilepath - Exact path of lambda deployment (.zip) file is uploaded (ex:lambda/backend.zip )






