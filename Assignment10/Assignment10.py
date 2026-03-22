# Write a program to read the file and create a customers list, where each element in the list is a dictionary 
# of information for a given customer. Provide an interface for the program above that allows the user to:
# Display company name, contact name, and phone number for all customers sorted by company name.
# Display contact name, company name, and phone number for all customers sorted by contact name.
# Search for a given company name or part of a name and display matching records with fields labeled.
# Search for a given contact name or part of a name and display matching records with fields labeled.
# For each of the above, use separate functions for each type of processing. Reuse functions where possible, such 
# as in sorting and searching. Avoid using global variables by passing parameters and returning results. Include 
# appropriate data validation and parameter validation. Add program and function documentation, consistent with 
# the documentation standards for your selected programming language.
import csv

# Load the csv file
def load_customers(filename):
    customers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # Read each row and add to the customers list
            for row in reader:
                customers.append(row)
    except:
        print("Could not open the file.")
    return customers

# Sorting functions
def sort_by_company(customers):
    # Return a new list sorted by company name
    return sorted(customers, key=lambda c: c["CompanyName"])

def sort_by_contact(customers):
    # Return a new list sorted by contact name
    return sorted(customers, key=lambda c: c["ContactName"])

# Display functions
def display_company_list(customers):
    # For each customer, print the company name, contact name, and phone number
    for c in customers:
        print("Company Name:", c["CompanyName"])
        print("Contact Name:", c["ContactName"])
        print("Phone:", c["Phone"])
        print("----------------------------------")

def display_contact_list(customers):
    # For each customer, print the contact name, company name, and phone number
    for c in customers:
        print("Contact Name:", c["ContactName"])
        print("Company Name:", c["CompanyName"])
        print("Phone:", c["Phone"])
        print("----------------------------------")

# Searching functions
def search_by_company(customers, term):
    results = []
    # Convert the search term to lowercase for easier searching
    term = term.lower()
    for c in customers:
        if term in c["CompanyName"].lower():
            results.append(c)
    return results

def search_by_contact(customers, term):
    results = []
    term = term.lower()
    for c in customers:
        if term in c["ContactName"].lower():
            results.append(c)
    return results

# Main program menu
def main():
    customers = load_customers("northwind.csv")
    # Check if customers were loaded successfully
    if len(customers) == 0:
        print("No customers loaded.")
        return
    while True:
        # Display the menu options
        print("Customer Menu")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search by company name")
        print("4. Search by contact name")
        print("5. Exit")
        choice = input("Enter choice: ")
        # If 1, sort by company and display
        if choice == "1":
            sorted_list = sort_by_company(customers)
            display_company_list(sorted_list)
        # If 2, sort by contact and display
        elif choice == "2":
            sorted_list = sort_by_contact(customers)
            display_contact_list(sorted_list)
        # If 3, ask for search term, search by company, and display results
        elif choice == "3":
            term = input("Enter company name or part of name: ")
            results = search_by_company(customers, term)
            display_company_list(results)
        # If 4, ask for search term, search by contact, and display results
        elif choice == "4":
            term = input("Enter contact name or part of name: ")
            results = search_by_contact(customers, term)
            display_contact_list(results)
        # If 5, exit the program
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")       
if __name__ == "__main__":
    main()