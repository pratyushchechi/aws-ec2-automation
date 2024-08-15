import boto3
import time

# Create an EC2 resource
ec2 = boto3.resource('ec2')

# Launch a new EC2 instance
instance = ec2.create_instances(
    ImageId='ami-04a81a99f5ec58529',  # Replace with the AMI ID of your choice
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Free-tier eligible instance type
    KeyName='monitoringssh'  # Replace with your existing key pair
)

# Print the ID of the new instance
instance_id = instance[0].id
print(f'Created EC2 Instance: {instance_id}')

# Wait until the instance is running
print('Waiting for the instance to enter the running state...')
instance[0].wait_until_running()

# Reload the instance attributes after it starts running
instance[0].reload()

# Stop the instance
print(f'Stopping EC2 Instance: {instance_id}...')
ec2.instances.filter(InstanceIds=[instance_id]).stop()

# Wait until the instance is stopped
print('Waiting for the instance to stop...')
instance[0].wait_until_stopped()

# Start the instance
print(f'Starting EC2 Instance: {instance_id}...')
ec2.instances.filter(InstanceIds=[instance_id]).start()

# Wait until the instance is running again
print('Waiting for the instance to start...')
instance[0].wait_until_running()

# Terminate the instance
print(f'Terminating EC2 Instance: {instance_id}...')
ec2.instances.filter(InstanceIds=[instance_id]).terminate()
print(f'Terminated EC2 Instance: {instance_id}')

# Adding Error Handling for Stopping the Instance:
try:
    ec2.instances.filter(InstanceIds=[instance_id]).stop()
    print(f'Successfully stopped EC2 Instance: {instance_id}')
except Exception as e:
    print(f'Error stopping instance: {e}')

