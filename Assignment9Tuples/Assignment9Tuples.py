# Write a program to read the file and create a customers list, where each element in the list is a customer list or tuple.
# Provide an interface for the program above that allows the user to: Display company name, contact name, and phone number 
# for all customers sorted by company name.Display contact name, company name, and phone number for all customers sorted by 
# contact name. Search for a given company name or part of a name and display matching records with fields labeled. Search 
# for a given contact name or part of a name and display matching records with fields labeled.
# For each of the above, use separate functions for each type of processing. Reuse functions where possible, such as in sorting 
# and searching. Avoid using global variables by passing parameters and returning results. Include appropriate data validation 
# and parameter validation.
import csv

# Load customers from file
def load_customers(filename):
    customers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                # Each row should become a tuple for immutability
                customers.append(tuple(row))
        return customers
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except Exception as e:
        print("Error reading file:", e)
        return []

# Display helper functions
def display_by_company(customers):
    sorted_list = sorted(customers, key=lambda c: c[1].lower())
    print("\nCustomers Sorted by Company Name:\n")
    for c in sorted_list:
        print(f"Company: {c[1]}")
        print(f"Contact: {c[2]}")
        print(f"Phone:   {c[9]}")
        print("-" * 40)

def display_by_contact(customers):
    sorted_list = sorted(customers, key=lambda c: c[2].lower())
    print("\nCustomers Sorted by Contact Name:\n")
    for c in sorted_list:
        print(f"Contact: {c[2]}")
        print(f"Company: {c[1]}")
        print(f"Phone:   {c[9]}")
        print("-" * 40)

# Search logic
def search_by_company(customers, term):
    term = term.lower()
    results = [c for c in customers if term in c[1].lower()]
    return results

def search_by_contact(customers, term):
    term = term.lower()
    results = [c for c in customers if term in c[2].lower()]
    return results

def display_search_results(results):
    if not results:
        print("No matching records found.\n")
        return
    print("\nSearch Results:\n")
    for c in results:
        print(f"Customer ID: {c[0]}")
        print(f"Company:     {c[1]}")
        print(f"Contact:     {c[2]}")
        print(f"Title:       {c[3]}")
        print(f"Address:     {c[4]}, {c[5]} {c[6]} {c[7]}")
        print(f"Country:     {c[8]}")
        print(f"Phone:       {c[9]}")
        print(f"Fax:         {c[10]}")
        print("-" * 50)

# Display menu
def print_menu():
    print("Customer Menu")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

# Main loop
def main():
    filename = "NorthwindCustomers.txt"
    customers = load_customers(filename)
    if not customers:
        return
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            display_by_company(customers)
        elif choice == "2":
            display_by_contact(customers)
        elif choice == "3":
            term = input("Enter company name or part of name: ").strip()
            if term:
                results = search_by_company(customers, term)
                display_search_results(results)
            else:
                print("Search term cannot be empty.")
        elif choice == "4":
            term = input("Enter contact name or part of name: ").strip()
            if term:
                results = search_by_contact(customers, term)
                display_search_results(results)
            else:
                print("Search term cannot be empty.")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number 1 through 5.")

if __name__ == "__main__":
    main()