import json
import os

output_dir = './ec2-no-tag-name'
output_file = os.path.join(output_dir, 'resources.json')

with open(output_file, 'r') as f:
    data = json.load(f)

instances = data
for instance in instances:
    instance_id = instance.get('InstanceId', 'Unknown ID')
    name_tag = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), 'No Name')
    print(f"Instance ID: {instance_id}, Name: {name_tag}")

