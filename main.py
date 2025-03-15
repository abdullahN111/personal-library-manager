import json


class BookCollection:
    """A class to manage the collection of books."""
    
    def __init__(self):
        """Initialize a new book collection with an empty list"""
        
        self.book_list = []
        self.storage_file = "data.json"
        self.read_from_file()
        
    def read_from_file(self):
        """Load saved books from a json file into memory or start with an empty collection"""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
            
    def save_to_file(self):
        """Store the current book collection to a json file"""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)
            
    def create_new_book(self):
        """Create a book in the collection by getting inputs from the user."""
        book_title = input("Enter book title: ")
        book_author = input(f"Who is the author of {book_title}: ")
        book_publication = input("Enter publication year: ")
        book_genre = input(f"What is the genre of {book_title}: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
   
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": book_publication,
            "genre": book_genre,
            "read": is_book_read
        } 
        
        self.book_list.append(new_book)
        self.save_to_file()
        print("\nBook added successfully. ✅\n")
        
        
    def remove_book(self):
        """Remove the book from collection using title."""
        book_title = input("Enter the title of the book you want to remove: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("\nBook removed successfully!\n")
                return
        print("\nBook not found!\n")
        
        
    def find_book(self):
        """Search for a book in collection using book title or author name."""
        search_type = input("\nSearch by:\n1. Title\n2. Author\n\nEnter your choice: ")
        search_text = input("Search here: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book['title'].lower()
            or search_text in book['author'].lower()
        ]
        
        if found_books:
            print("\nMatching books...\n")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
                
        else:
            print("\nNo matching books found!\n")
        
        
    def show_all_books(self):
        """Showing the collection of books"""
        print("\n<--Our Books-->\n")
        for index, book in enumerate(self.book_list):
            print(f"{index+1}. {book['title']} by {book['author']} ({book['year']})")
        
    
    
    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            print("\n\n📚 Welcome to Your Book Collection Manager! 📚\n")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. View all books")
            print("5. Exit")
            user_choice = input("\nPlease choose an option (1-5): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.remove_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.show_all_books()
            elif user_choice == "5":
                self.save_to_file()
                print("\nThank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()