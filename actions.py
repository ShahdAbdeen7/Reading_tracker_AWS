import datetime
from setup_DB2 import get_connection
from notifier import send_sns_notification
from logger import log_cloudwatch



def add_book():
	title = input("Enter the book title: \n")
	total = input("Enter the number of book's pages: \n")
	pages = input("Enter the number of pages read: ")
	date_Read = datetime.date.today()
	

	conn = get_connection()
	cursor = conn.cursor()

## check if the book already exists or completed
	cursor.execute("select sum(pages_read), max(total_pages) from reading_log where book_title = %s", (title,))
	result = cursor.fetchone()
	pages_read = result[0] or 0
	total_pages = result[1] or 0
	if total_pages and pages_read>total_pages:
		print("You can't add more logs to this book. You have already completed reading this book!")
		conn.close()
		return
	elif pages_read==total_pages:
## send sns notification
		send_sns_notification(title)





	cursor.execute("insert into reading_log(book_title, total_pages, pages_read, date_read) values (%s, %s, %s, %s )", (title, total, pages, date_Read))
	print(f"{pages} Total number of pages read for {date_Read}")
	conn.commit()
	conn.close()
	log_cloudwatch(f"Book added: {title} with {pages} pages read. ")



def delete_book(): ## deletion for an entire book logs

	id = input("Enter the id of the book you want to delete: \n")
	
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("delete from reading_log where id= %s", (id,))
	print("The record with this id has been deleted successfully!")
	conn.commit()
	conn.close()
	log_cloudwatch(f"Book Deleted: ID {id}")





def update_info():
	id = input("Enter the ID of the book you want to update info for: \n")
	pages = input("Enter the new number of pages you read for this record: \n")
	
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("update reading_log set pages_read = %s where id= %s", (pages, id))
	print("Record info has been updated successfully!")
	conn.commit()
	conn.close()
	log_cloudwatch(f"Info Updated: {id}: Book with {pages} pages read today has been updated!")




##update status for all records and books










def log_progress():
	

	conn = get_connection()
	cursor = conn.cursor()
	
	cursor.execute("select distinct book_title from reading_log")
	books = cursor.fetchall()

	print("\n Your reading list:")

	for book in books:
		title = book[0]
		cursor.execute("""
			select SUM(pages_read),
			max(total_pages)
			from reading_log
			where book_title = %s
			""",(title,))
		result = cursor.fetchone()
		pages_read = result[0] or 0
		total_pages = result[1] or 0
		status = 'complete' if pages_read >=total_pages and total_pages  else 'in-progress'
		percent = (pages_read / total_pages) * 100 if total_pages else 0
		cursor.execute("update reading_log set status = %s where book_title = %s", (status,title))
		

		print(f"- {title}: {pages_read}/{total_pages} pages read ({percent:.1f}%)")
	
		log_cloudwatch(f"{pages_read} Logged pages read for book - {title}")



	conn.commit()
	conn.close()
	



def show_books():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT id, book_title, pages_read, total_pages, date_read FROM reading_log")
	books = cursor.fetchall()
	for book in books:
		cursor.execute("select sum(pages_read), max(total_pages) from reading_log where book_title = %s", (book[1],))

		result = cursor.fetchone()
		total_read = result[0] or 0
		total_pages = result[1] or 0

		status = 'completed' if total_read>=total_pages and total_pages else 'in-progress'

		cursor.execute("UPDATE reading_log SET status = %s WHERE id = %s", (status, book[0]))

		print(f"{book[0]}: {book[1]} - {book[2]} on {book[4]} | {status}")
	conn.commit()
	conn.close()


