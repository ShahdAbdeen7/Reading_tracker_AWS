import boto3, time, datetime
from config import REGION, LOG_GROUP, LOG_STREAM



def log_cloudwatch(message):
	## connect to cloudwatch logs
	logs = boto3.client("logs", region_name = 'eu-north-1')
	
	## get current sequence token
	response = logs.describe_log_streams(
		logGroupName = LOG_GROUP,
		logStreamNamePrefix = LOG_STREAM

)


	sequence_token = response["logStreams"][0].get("uploadSequenceToken")

	## create the log message

	event = {
		'logGroupName': LOG_GROUP,
       		'logStreamName': LOG_STREAM,
       		'logEvents': [{
            	'timestamp': int(time.time() * 1000),
            	'message': message
      		  }]

	}


	## aws will give you a token. add it
	if sequence_token:
       		event['sequenceToken'] = sequence_token

	
	## Send the log to AWS
	logs.put_log_events(**event)




