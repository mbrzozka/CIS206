# Allow a use to enter first name and last name into two separate 
# variables. Then display the values in the order of last name, 
# first name.
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Your name is:", last_name + ",", first_name)
main()