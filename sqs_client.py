import boto3

from app_settings import QUEUE_URL


class SQSClient:
    def __init__(self, ):
        self.client = boto3.client('sqs')

    def send_message(self, data):
        self.client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=data
        )

    def receive_message(self):
        return self.client.receive_message(
            QueueUrl=QUEUE_URL,
            AttributeNames=['All'],
            MaxNumberOfMessages=10,
            VisibilityTimeout=30,
            WaitTimeSeconds=10,
        )
