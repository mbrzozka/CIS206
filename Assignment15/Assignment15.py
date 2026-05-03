import json

# Load books from JSON file
def load_books():
    with open("books.json", "r") as file:
        data = json.load(file)
    return data["books"]

# Display list of books
def display_books(books):
    print("\n--- BOOK LIST -------------")
    for b in books:
        print(f"{b['title']} ({b['year']}) by {b['author']}")
    print("---------------------------\n")

# Find books by title (not case sensitive)
def find_book(books, title):
    for b in books:
        if b["title"].lower() == title.lower():
            return b
    return None

def main():
    books = load_books()
    display_books(books)

    while True:
        title = input("Enter a book title (or 'exit' to quit): ")
        # If user types exit, break loop and end program
        if title.lower() == "exit":
            break

        book = find_book(books, title)
        # If book is found, print details, otherwise print not found message
        if book:
            print(f"FOUND: {book['title']} by {book['author']} ({book['year']})\n")
        else:
            print(f"'{title}' not found.\n")

if __name__ == "__main__":
    main()