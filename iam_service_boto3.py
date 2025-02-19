

#Import all the modules and Libraries
import boto3

#Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

#Open IAM console
iam_console = aws_management_console.client(service_name="iam")

#Use boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation)

result = iam_console.get_user()
print(result['User']['UserName'])

for tag_key in result['User']['Tags']:
    if tag_key['Key'] == "AKIATG6MGK7SLXGYB6PB":
        print(f"Yes your tag key is present : {tag_key["Key"]}")
    else:
        print(f"No Your tag key is not present")
    # print(tag_key['Key'])