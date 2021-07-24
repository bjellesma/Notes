* The majority of applications are developed on **Elastic Compute Cloud** known in AWS as EC2
* Each AWS Service is given an **Amazon Resource Name** (ARN)
* AWS Services use **Amazon Relational Database Service** (Amazon RDS) to store data and connect on port 5432
* All services are configured using the AWS Management Console
* AWS CLI is good for shell scripting and interacting with other services
    * Not used frequently for developers but used more for ops engineers
* AWS **Software Development Kit** (SDKs) are used with several popular programming languages
* Start working with AWS
    * Install Node 14+
    * Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
    * Create an AWS account
    * Create an AWS Access Key
    * use `aws configure` to be prompted to enter both your access key and secret key
    * Use the command `aws ec2 describe-instances` to ensure that your instances are setup correctly. Because we have no instances, this command should be empty

```json
{
    "Reservations": []
}
```