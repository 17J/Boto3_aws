# #import modules and libraries
# import boto3
# from pprint import pprint

# #Open Management Console
# aws_management_console  = boto3.session.Session(profile_name="default")

# #Open ec2 console
# aws_ec2 = aws_management_console.client(service_name="ec2")
# instance_idss = []


# #use boto3 docs
# describe_instance  = aws_ec2.describe_instances()

# for instance_list in describe_instance['Reservations']:
#     for instance_ids in instance_list['Instances']:
#         # pprint(instance_ids['InstanceId'])
#         instance_idss.append(instance_ids['InstanceId'])
        

        
# print(instance_idss)
# # response = client.terminate_instances(
# #     InstanceIds=[]s

    
# # )

# # respo = aws_ec2.terminate_instances(
# #     InstanceIds=[instance_idss]
    
# # )

#start instance
response = aws_ec2.start_instances(
    InstanceIds='instanceid'
)


#stop instance
response = aws_ec2.stop_instances(
    InstanceIds='instanceid'
)
