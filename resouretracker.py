import boto3

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id='give access key',
    aws_secret_access_key='give access key',
    region_name='ap-south-1'
)

# Create a client for the EC2 service
ec2_client = session.client('ec2')

# Execute the describe-instances command
response = ec2_client.describe_instances()

# Get Instance type and Instance id of available ec2 in the given region.
for i, reservation in enumerate(response['Reservations']):
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]

        print(f"The Available EC2 in AWS are \n{i+1}\t The instance_id = {instance_id}\t instance_type = {instance_type}")

# Create a client for the s3 service        
s3_client = session.client('s3')

# Execute the S3 list-buckets command
s3_response = s3_client.list_buckets()

for i, bucket in enumerate(s3_response['Buckets']):
    bucket_name = bucket['Name']
    print(f"The Available buckets in AWS are \n{i + 1} \t {bucket_name}")


# Create a client for iam service
iam_client = session.client('iam')

# Execute the list users in iam command
iam_response = iam_client.list_users()


print("The Iam Users available in AWS are")
for i, user in enumerate(iam_response['Users']):
    iam_user_name = user['UserName']
    iam_user_id = user['UserId']
    print(f"{i+1}\tUser-id is {iam_user_id} and name is {iam_user_name}")



    