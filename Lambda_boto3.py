import boto3

Region = "us-east-1"
AMI = "ami-01b799c439fd5516a"
Key_Pair = 'Project_6'
Sg = 'sg-0c1799326c382209f'

ec2 = boto3.client('ec2', region_name=Region )

response = ec2.run_instances(
    ImageId=AMI,
    InstanceType='t2.micro',
    KeyName=Key_Pair,
    MaxCount=3,
    MinCount=3,
    SecurityGroupIds=[Sg],
)

Instance_ids = [instance["InstanceId"] for instance in response["Instances"]]

ec2.instances.filter(InstanceIds=Instance_ids).stop()

print(f"Instances stopped: {Instance_ids}")