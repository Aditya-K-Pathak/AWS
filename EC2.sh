#!usr/bin/bash

aws configure

# AWS Access Key ID:<Input>
# AWS Secret Access Key:<Input>
# Default region name:<Input>
# Default output format:<Input>

# Create an Instance
aws ec2 run-instances --image-id <Value> --instance-type <value>
# Starting a instance
aws ec2 start-instances --instance-id <Value>
# Stop a instance
aws ec2 stop-instances --instance-id <Value>
# Terminate a instance
aws ec2 terminate-instances --instance-id <Value>
# Stop a instance
aws ec2 describe-instances