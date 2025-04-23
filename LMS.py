# Library Management System
# Developed by Alexandru Carp
# Module: ACCA5036

# List to store all book records
books_list = []

# Function to add a new book
def add_book():
    print("\n--- Add a New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "status": "available"
    }
    books_list.append(book)
    print(f"Book '{title}' added successfully!\n")

# Function to search for books
def search_book():
    print("\n--- Search for a Book ---")
    keyword = input("Enter a keyword (title, author, genre): ").strip().lower()
    found_books = []
    for book in books_list:
        if (keyword in book["title"].lower() or
            keyword in book["author"].lower() or
            keyword in book["genre"].lower()):
            found_books.append(book)
    if found_books:
        print("\nBooks Found:")
        for book in found_books:
            print_book_info(book)
    else:
        print("No books found matching that keyword.\n")

# Function to display all books
def display_books():
    print("\n--- Display All Books ---")
    if books_list:
        for book in books_list:
            print_book_info(book)
    else:
        print("No books available in the library.\n")

# Function to update book information
def update_book():
    print("\n--- Update Book Information ---")
    title = input("Enter the title of the book to update: ").strip()
    for book in books_list:
        if book["title"].lower() == title.lower():
            print("Book found. What would you like to update?")
            field = input("Enter field to update (title/author/genre): ").strip().lower()
            if field in ["title", "author", "genre"]:
                new_value = input(f"Enter new {field}: ").strip()
                book[field] = new_value
                print(f"Book {field} updated successfully!\n")
            else:
                print("Invalid field selected.\n")
            return
    print("Book not found.\n")

# Function to check out / check in a book
def check_in_out_book():
    print("\n--- Check In / Check Out a Book ---")
    title = input("Enter the title of the book: ").strip()
    for book in books_list:
        if book["title"].lower() == title.lower():
            if book["status"] == "available":
                book["status"] = "checked out"
                print(f"Book '{title}' has been checked out.\n")
            else:
                book["status"] = "available"
                print(f"Book '{title}' has been checked in.\n")
            return
    print("Book not found.\n")

# Function to delete a book
def delete_book():
    print("\n--- Delete a Book ---")
    title = input("Enter the title of the book to delete: ").strip()
    for book in books_list:
        if book["title"].lower() == title.lower():
            books_list.remove(book)
            print(f"Book '{title}' deleted successfully.\n")
            return
    print("Book not found.\n")

# Helper function to print book information
def print_book_info(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Status: {book['status']}")

# Main menu loop
def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display All Books")
        print("4. Update Book Information")
        print("5. Check In/Out Book")
        print("6. Delete Book")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            display_books()
        elif choice == "4":
            update_book()
        elif choice == "5":
            check_in_out_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

# Run the main program
if __name__ == "__main__":
    main()
