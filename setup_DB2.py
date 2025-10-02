### set up the database, and table(s)


## import necessary libraries
import mysql.connector
from config import HOST, USER, PASSWORD, DB_NAME


## Create DB connection

def create_connection():
	return mysql.connector.connect(
		host = HOST,
		user = USER,
		password = PASSWORD,
)


## create DB if it doesn't exist
def create_DB():
	conn = create_connection()
	cursor = conn.cursor()
	
	cursor.execute("create database if not exists read_db")
	print("Database is created successfully!")

	



## create connection to the RDS mysql database
	
def get_connection():
	return mysql.connector.connect(
		host = HOST,
		user = USER,
		password = PASSWORD,
		database = DB_NAME

)




## create set up connection and tables through connection to the RDS database engine


def create_tables():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("""
		create table if not exists reading_log (
 				  id INT AUTO_INCREMENT PRIMARY KEY,
 				  book_title VARCHAR(255),
    				  total_pages INT,
   				  pages_read INT,
    				  date_read DATE,
    			 	  status VARCHAR(20) DEFAULT 'in-progress'
					            )
				                        """)

		
	cursor.execute('''
       		 create table if not exists progress(
           			 id INT AUTO_INCREMENT PRIMARY KEY,
          		 	 book_id INT,
            			 pages_read INT,
            			 date DATE,
           			 #OREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
   						     )
   							 ''')






	conn.commit()
	print("Database and Table created successfully")
	cursor.close()
	conn.close()


def set_up():
	create_DB()
	create_tables()

 		
#print("Database and tables are created successfully!")