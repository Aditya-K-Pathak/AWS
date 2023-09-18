# A class that implement a few important function of SNS Simple Notification Service
import boto3

class SNS:
    def __init__(self) -> any:
        self.aws = boto3.session.Session(profile_name = "default")
        self.sns = self.aws.client("sns")

    def create_topic(self, name: str) -> dict:
        return self.sns.create_topic(Name = name)
    
    def delete_topic(self, topicArn: str) -> None:
        return self.sns.delete_topic(TopicArn = topicArn)

    def subscribe(self, topicArn: str, protocol: str, endpoint: str) -> dict:
        return self.sns.subscribe(TopicArn = topicArn, Protocol = protocol, Endpoint = endpoint)
    
    def unsubscribe(self, subscriptionArn: str) -> None:
        return self.sns.unsubscribe(SubscriptionArn = subscriptionArn)
    
    def list_subscriptions(self, NextToken: str = "") -> dict:
        if NextToken != "":return self.sns.list_subscriptions(NextToken = NextToken)
        else:return self.sns.list_subscriptions()
    
    def list_topics(self, NextToken: str = "") -> dict:
        if NextToken != "":return self.sns.list_topics(NextToken = NextToken)
        else:return self.sns.list_topics()
    
    def publish(self, TopicArn: str, Message: str, Subject: str) -> dict:
        return self.sns.publish(TopicArn = TopicArn, Message = Message, Subject = Subject)
