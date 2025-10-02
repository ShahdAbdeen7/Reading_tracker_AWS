import boto3
from config import REGION, SNS_TOPIC_ARN




### check for sns notification. only when status is completed

def send_sns_notification(book_title):
    sns = boto3.client('sns', region_name= REGION)  #
    sns.publish(
        TopicArn= SNS_TOPIC_ARN,
        Subject="Book Completed!",
        Message=f"Finally Shahd! You've finished reading '{book_title}'!"
    )
    print("📬 SNS notification sent!")
