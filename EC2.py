# A class that implement a few important function of EC2
import boto3

class EC2:
    def __init__(self):
        self.aws = boto3.session.Session(profile_name = "default")
        self.ec2 = self.aws.client("ec2")

    def create_instance(self, ImageId: str, maxcount: int, InstanceType: str = "t2.micro"):
        return self.ec2.run_instances(ImageId = ImageId, MinCount = 1, MaxCount = maxcount, InstanceType = InstanceType)

    def start_instance(self, INSTANCE_ID: list):
        return self.ec2.start_instances(InstanceIds = INSTANCE_ID)
    
    def stop_instance(self, INSTANCE_ID: list[str]):
        return self.ec2.stop_instances(InstanceIds = INSTANCE_ID)
    
    def terminate_instance(self, INSTANCE_ID: list[str]):
        return self.ec2.terminate_instances(InstanceIds = INSTANCE_ID)
    