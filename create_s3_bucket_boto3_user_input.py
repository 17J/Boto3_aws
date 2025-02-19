#import modules and libraries
import boto3
#aws management console
aws_management_console = boto3.session.Session(profile_name="default")

#get s3 bucket
aws_s3_bucket = aws_management_console.client(service_name="s3")

#create a bucket

# bucket_list = ['abc-test-demo-17071','abc-test-demo-17072','abc-test-demo-17073']


#create bucket 5 with input 

for bucket in range(5):
    bucket_names = input("Enter Your Bucket Name, Name Must be Unique : ")
    
    bucket_name = bucket
    print(f"Bucket name is : {bucket_names}")
    try:
        res = aws_s3_bucket.create_bucket(
            Bucket = bucket_names,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1',
            }
        )
        print(f"Bucket Has Been added Successfully: {bucket_names}")
    except NameError as e:
        print(f"Bucket name is already present, name must be unique: {e}")
        
        
        
