#Import modules and Libraries
import boto3
from pprint import pprint

#Open Management Console

aws_management_console = boto3.session.Session(profile_name="default")

#Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")


#Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation)
result = ec2_console.describe_instances()


for instance_id in result['Reservations']:
    for key_names in instance_id['Instances']:
        print(key_names['InstanceId'])
