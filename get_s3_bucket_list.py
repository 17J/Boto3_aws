#import all package and libraries
import boto3
from pprint import pprint

#open aws management console
aws_management_console = boto3.session.Session(profile_name="default")

#open s3 bucket list
aws_s3 = aws_management_console.client(service_name="s3")

list_buckets = []

#get list of bucket
#go with boto3 docs     

#get bucket name example

# result = aws_s3.list_buckets()
# for list_bucket in result['Buckets']:
#     # print(f"Name of Bucket is: {list_bucket['Name']}")
#     list_buckets.append(list_bucket['Name'])




# delete bucket 

# for bucket in list_buckets:
#     bucket_name = bucket
#     print(f"bucket name is {bucket_name}")
    
#     try:
#         res = aws_s3.delete_bucket(
#             Bucket = bucket_name
#         )
#         print(f" Bucket: {bucket_name}")
#     except NameError as e:
#         print(f"Error deleing bucket {bucket_name} : {e}")


#create bucket by list

# respo = aws_s3.create_bucket(
    
# )

name_of_bucket = ["first-bucket-list-boto3-17077", "second-bucket-list-boto3-17087","third-bucket-list-boto3-88771"]

# for bucket in name_of_bucket:
#     bucket_name = bucket
#     print(f"bucket name is {bucket_name}")
    
#     try:
#         res = aws_s3.create_bucket(
#             Bucket = bucket_name,
#             CreateBucketConfiguration={
#                 'LocationConstraint': 'ap-south-1',
#             }
#         )
#     except NameError as e:
#         print(f"Bucket name is already present please enter new name {bucket_name} : {e}")



#delete created bucket all these three

# for bucket in name_of_bucket:
#     bucket_name = bucket
#     print(f"bucket name {bucket_name}")
    
#     try:
#         res = aws_s3.delete_bucket(
#             Bucket = bucket_name
#         )
#         print(f"Bucket is delete successfully :{bucket_name}")
#     except NameError as e:
#         print(f"Bucket name not present {bucket_name} : {e}")