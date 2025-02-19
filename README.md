# Boto3_aws
#To Use Boto3 First Of All boto3 module in your package
#setup aws credentials properly 

#sample format for it

#import modules and Library
import boto3

#aws management console
aws_management_console = boto3.session.Session(profile_name="default")

#uses aws resources
aws_ec2_list = aws_management_console.client(service_name="ec2")

#get list of or other things go for "https://boto3.amazonaws.com/v1/documentation/api/"      boto3 document 
