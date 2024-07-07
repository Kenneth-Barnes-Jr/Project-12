--- Foundation ---

import boto3

def lambda_handler(event, context):

    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    instance_ids_to_stop = ['< Instance 1 >', '< Instance 2 >','< Instance 3 >'] 
   
    ec2.stop_instances(InstanceIds=instance_ids_to_stop)
   
    print(f"Instances stopped: {instance_ids_to_stop}")