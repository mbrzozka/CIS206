import sqlite3

# Connect to the database and return the connection object
def connect_db(db_name):
    return sqlite3.connect(db_name)

# Makes sure the user inputs a valid number within the set range
def get_valid_number(prompt, min_value, max_value):
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Enter a valid number.")
        else:
            value = int(value)
            if value < min_value or value > max_value:
                print("Enter a valid number.")
            else:
                return value

# Makes sure the user inputs a valid choice from the given options
def get_valid_choice(prompt, valid_choices):
    while True:
        value = input(prompt).upper()
        if value in valid_choices:
            return value
        print("Invalid choice.")

# Get a list of all tables in the database
def get_table_list(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]

# Display the contents of the selected table with numbered rows
def display_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    # Column names
    columns = [col[1] for col in cursor.fetchall()]
    cursor.execute(f"SELECT * FROM {table_name};")
    # All rows
    rows = cursor.fetchall()
    print("\nColumns:", columns)
    for i, row in enumerate(rows, start=1):
        # Numbered rows
        print(f"{i}: {row}")
    return columns, rows

# Insert a new record into the selected table
def insert_record(connection, table_name, columns):
    cursor = connection.cursor()
    values = []
    for col in columns:
        # Ask for each field
        values.append(input(f"{col}: "))
    placeholders = ",".join(["?"] * len(columns))
    query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders});"
    cursor.execute(query, values)
    connection.commit()
    print("Record inserted.")

# Update an existing record in the selected table
def update_record(connection, table_name, columns, rows):
    cursor = connection.cursor()
    if len(rows) == 0:
        print("No rows to update.")
        return
    row_num = get_valid_number("Row number to update: ", 1, len(rows))
    # Assumes first column is PK because I need it for the WHERE clause
    row_id = rows[row_num - 1][0]
    for i, col in enumerate(columns):
        print(f"{i+1}. {col}")
    col_num = get_valid_number("Column number: ", 1, len(columns))
    column_name = columns[col_num - 1]
    new_value = input(f"New value for {column_name}: ")
    query = f"UPDATE {table_name} SET {column_name}=? WHERE {columns[0]}=?;"
    cursor.execute(query, (new_value, row_id))
    connection.commit()
    print("Record updated.")

# Delete a record from the selected table
def delete_record(connection, table_name, columns, rows):
    cursor = connection.cursor()
    if len(rows) == 0:
        print("No rows to delete.")
        return
    row_num = get_valid_number("Row number to delete: ", 1, len(rows))
    # Assumes first column is PK
    row_id = rows[row_num - 1][0]
    query = f"DELETE FROM {table_name} WHERE {columns[0]}=?;"
    cursor.execute(query, (row_id,))
    connection.commit()
    print("Record deleted.")

def main(db_name):
    connection = connect_db(db_name)
    tables = get_table_list(connection)
    # Only customers, employees, and products tables allowed to be accessed
    allowed_table_names = ["customers", "employees", "products"]
    tables = [table for table in tables if table.lower() in allowed_table_names]
    # If no allowed tables are found, print message and exit
    if len(tables) == 0:
        print("No allowed tables found (Customers, Employees, Products).")
        connection.close()
        return
    for i, table in enumerate(tables, start=1):
        print(f"{i}. {table}")
    table_choice = get_valid_number("Select table number: ", 1, len(tables))
    table_name = tables[table_choice - 1]
    columns, rows = display_table(connection, table_name)
    print("\n(I)nsert  (U)pdate  (D)elete")
    choice = get_valid_choice("Choice: ", ["I", "U", "D"])
    if choice == "I":
        insert_record(connection, table_name, columns)
    elif choice == "U":
        update_record(connection, table_name, columns, rows)
    elif choice == "D":
        delete_record(connection, table_name, columns, rows)
    connection.close()

main("Northwind.db")