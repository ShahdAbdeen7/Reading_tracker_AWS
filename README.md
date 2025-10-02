This is a simple app that lets you keep track of your reading habits, log the progress to Amazon CloudWatch, and save the records into Amazon RDS. If it happens and you finish reading a book, and Amazon sns notification is sent to your email address.
I used the seperation of concerns principle to divide the code (just a way to know exactly where to look when something needs to be changed)


#what it does
add (also delete and modify ) records of pages you read during a day of a certain book.
store these records in Amazon RDS.
send Amazon sns notification when a book is completed.
log the process into Amazon CloudWatch.



#Technologies I used:
Amazon RDS (MYSQl engine)
Amazon SNS
Amazon cloudWatch
Python + boto3 (sdk for python with aws)
AWS CLI


I used the seperation of concerns to divide the code (just a way to know exactly where to look when something needs to be changed)

#Files:
Main app = for user interaction
Db = db connection and set up
Actions = add, delete , modify and view
Notifier = sns notification
Logger = cloud watch logs
Config = configuration variables

#How to run
clone the repository
install requirements:
boto3
mysql-connector-python

