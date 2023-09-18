# A Shell program to use some sns features

#!usr/bin/bash

aws configure

# AWS Access Key ID:<Input>
# AWS Secret Access Key:<Input>
# Default region name:<Input>
# Default output format:<Input>

# Create Topic
aws sns create-topic --name <input>
# Delete Topic
aws sns delete-topic --topic-arn <input>
# Subscribe
aws sns subscribe --topic-arn <input> --protocol <input> --endpoint <input>
# Unsubscribe
aws sns unsubscribe --subscription-arn <input>
# List Subscriptions
aws sns list-subscriptions --next-token <input: not required>
# List topics
aws sns list-topics --next-token <input: not required>
# Publish
aws sns publish -topic-arn <input> --subject  <input> --message <input>