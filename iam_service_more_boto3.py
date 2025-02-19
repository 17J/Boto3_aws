#import modules and library
import boto3
from pprint import pprint #this module for better view of dict output

#aws management console
aws_management_console = boto3.session.Session(profile_name="default")

#iam service

aws_iam = aws_management_console.client(service_name="iam")

#create iam account with helps of docs https://boto3.amazonaws.com/v1/
#here i am gonna create user account by user input name


# for iam_account in range(5):
#     iam_name = input("Enter a User Name: ")
#     try:
#         response = aws_iam.create_user(
#             UserName = iam_name
#         )
#         print(f"Username is added {iam_name}")
#     except NameError as e:
#         print(f"Please Enter Accurate Name: {e}")
        
        
#Delete 5 Username by User input

# for iam_user_delete in range(5):
#     iam_user_name = input("Enter a User Name: ")
    
    
#     try:
#         response = aws_iam.delete_user(
#             UserName = iam_user_name
#         )
#         pprint(f"Username has been removed: {iam_user_name}")
#     except NameError as e:
#         pprint(f"Please Give Correct Username: {e} Your Entered Username does not exists")
        
        
#get list of iam username

res = aws_iam.list_users()
output_user_name = []

for user_name_list in res['Users']:
    # pprint(user_name_list['UserName'])
    output_user_name.append(user_name_list['UserName'])
    
print(output_user_name)
