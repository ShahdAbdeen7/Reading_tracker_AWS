##put all config vars here - so its easier to just reuse them. Also, capitalize everything, painful, but bear it. 

HOST = "book-db.cby44yagst22.eu-north-1.rds.amazonaws.com"
USER = "admin"
PASSWORD = "StrongPassword123!"
DB_NAME = "read_db"

REGION = "eu-north-1"
SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:553424000686:book-finished-notification"
LOG_GROUP = "reading_tracker_logs"
LOG_STREAM = "tracker_log"




	
def get_connection():
	return mysql.connector.connect(
		host = HOST,
		user = USER,
		password = PASSWORD,
		database = DB_NAME

)




	