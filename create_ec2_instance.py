# #import modules and libraries
# import boto3
# #aws management console
# aws_management_console = boto3.session.Session(profile_name="default")
# #create ec2 service
# create_ec2 = aws_management_console.client(service_name="ec2")
# #use boto3 docs

# response = create_ec2.run_instances(
#     ImageId="ami-0ddfba243cbee3768",
#     InstanceType="t2.micro",
#     MaxCount=1,
#     MinCount=1
# )