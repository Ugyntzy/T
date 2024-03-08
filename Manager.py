# LibraryManager.py

# Initialize empty data structures
books_list = []  # List to store book titles
authors_set = set()  # Set to store unique author names
books_dict = {}  # Dictionary to map titles to authors

# Add three books to the library
books_list.append("The Great Gatsby")
authors_set.add("F. Scott Fitzgerald")
books_dict["The Great Gatsby"] = "F. Scott Fitzgerald"

books_list.append("To Kill a Mockingbird")
authors_set.add("Harper Lee")
books_dict["To Kill a Mockingbird"] = "Harper Lee"

books_list.append("1984")
authors_set.add("George Orwell")
books_dict["1984"] = "George Orwell"

# Search for a book
search_title = input("Enter the title of the book you want to search for: ")
if search_title in books_list:
    author = books_dict.get(search_title)
    print(f"Book found! Title: {search_title}, Author: {author}")
else:
    print(f"Book '{search_title}' not found.")

# Display all books
print("\nAll books in the library:")
for title in books_list:
    print(title)

# Remove a book
remove_title = input("\nEnter the title of the book you want to remove (or press Enter to skip): ")
if remove_title in books_list:
    author_to_remove = books_dict.pop(remove_title)
    books_list.remove(remove_title)
    authors_set.discard(author_to_remove)
    print(f"Book '{remove_title}' removed successfully.")
else:
    print(f"Book '{remove_title}' not found.")
