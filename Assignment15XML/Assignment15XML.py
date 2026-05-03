import xml.etree.ElementTree as ET

# Load books from XML file
def load_books_xml():
    # Parse XML file and get root element
    tree = ET.parse("books.xml")
    root = tree.getroot()

    books = []
    # For each book, extract title, author, and year
    for book in root.findall("book"):
        title = book.find("title").text
        author = book.find("author").text
        year = int(book.find("year").text)
        books.append({"title": title, "author": author, "year": year})
    return books

# Display the list of books
def display_books(books):
    print("\n--- BOOK LIST (XML) ---------------")
    for b in books:
        print(f"{b['title']} ({b['year']}) by {b['author']}")
    print("------------------------------------\n")

# Search books by title (not case sensitive)
def find_book(books, title):
    for b in books:
        # If title matches, return book details
        if b["title"].lower() == title.lower():
            return b
    return None

def main():
    books = load_books_xml()
    display_books(books)

    while True:
        title = input("Enter a book title (or 'exit' to quit): ")
        # If user types exit, break and end program
        if title.lower() == "exit":
            break

        book = find_book(books, title)
        # If book is found print details, otherwise print not found message
        if book:
            print(f"FOUND: {book['title']} by {book['author']} ({book['year']})\n")
        else:
            print(f"'{title}' not found.\n")

if __name__ == "__main__":
    main()
