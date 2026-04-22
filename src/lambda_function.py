import json
import urllib
import urllib.request
import boto3
import os

region = os.getenv('EC2_REGION')
instances = [os.getenv('INSTANCE')]
slack_url = os.getenv('SLACK_URL')

ec2 = boto3.client('ec2', region_name=region)

def post_slack(message):
    
    send_data = {
        "text": message,
    }
    
    send_text = json.dumps(send_data)
    request = urllib.request.Request(
        slack_url, 
        data=send_text.encode('utf-8'), 
        method="POST"
    )
    with urllib.request.urlopen(request) as response:
        response.read().decode('utf-8')

def lambda_handler(event, context):

    # ec2.stop_instances(InstanceIds=instances)
    post_slack('EC2 Stoped')

