from setup_DB2 import create_tables
from actions import add_book, delete_book, update_info, log_progress, show_books


def main():
	print("Hey, I hope you had a nice time reading some pages.\n ")
	print("What do you want to do? \n 1. Add a book \n 2. Delete a book \n 3. Update book's info \n 4. Log reading progress \n 5. Show all books \n 6. Exit!")

	choice = input("Choose an action: ")
	if choice == "1":
		add_book()
	elif choice == "2":
		delete_book()
	elif choice == "3":
		update_info()
	elif choice == "4":
		log_progress()
	elif choice == "5":
		show_books()
	elif choice == "6":
		print("HAVE A GOOD DAY! BYE!") 
		
	else:
		print("Invalid option!")
	
	




if __name__ == "__main__":
	main()