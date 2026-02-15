# Create a program that asks users for their weight in pounds and their height in feet and inches. 
# Calculate and display their BMI. Format the output to one decimal place. Include a legend that 
# displays value ranges for underweight, normal, and overweight.
# Body mass index formula (Wikipedia): weight / height^2 * 703
# Expressed in units of lbs/in^2
def calculate_bmi(weight_pounds, height_feet, height_inches):
    # 1. Validate data type  
    if not isinstance(weight_pounds, (int, float)):
        raise TypeError("Weight must be a numeric value.")
    if not isinstance(height_feet, int):
        raise TypeError("Height (feet) must be an integer.")
    if not isinstance(height_inches, int):
        raise TypeError("Height (inches) must be an integer.")
    # 1. Validate parameter range
    if weight_pounds <= 0:
        raise ValueError("Weight must be greater than zero.")
    if height_feet < 0:
        raise ValueError("Height (feet) cannot be negative.")
    if not (0 <= height_inches < 12):
        raise ValueError("Height (inches) must be between 0 and 11.")
    # Convert height to inches
    total_height_inches = (height_feet * 12) + height_inches
    if total_height_inches == 0:
        raise ValueError("Total height cannot be zero.")
    # Calculate BMI
    bmi = (weight_pounds / (total_height_inches ** 2)) * 703
    return bmi

def bmi_category(bmi):
    if not isinstance(bmi, (int, float)):
        raise TypeError("BMI must be numeric.")
    if bmi <= 0:
        raise ValueError("BMI must be greater than zero.")
    # 3. Nested If Statament
    if bmi < 25:
        if bmi < 18.5:
            return "Underweight"
        else:
            return "Normal weight"
    else:
        return "Overweight"

def display_results(bmi, category):
    # Validate data type and range
    assert isinstance(bmi, (int, float)) and bmi > 0, "Invalid BMI passed to output function."
    # Check that category is not an empty string
    assert isinstance(category, str) and category.strip(), "Invalid category passed to output function."
    # Print info
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"BMI category: {category}")
    print("\nBMI Legend, according to the World Health Organization (WHO):")
    print("Underweight: Less than 18.5")
    print("Normal weight: 18.5 - 24.9")
    print("Overweight: 25 - 29.9")
    print("Obese: 30 and above")

def display_bmi_table():
    print("\nBMI Table:")
    print("-" * 102)
    # Header row
    print("Ht/Wt:", end="")
    weight = 100
    while weight <= 250:
        print("  " + str(weight), end=" ")
        weight += 10
    print()
    print("-" * 102)
    # Rows for heights with calculated BMI values
    height = 58
    while height <= 76:
        print(str(height) + " in:", end="")
        weight = 100
        while weight <= 250:
            feet = height // 12
            inches = height % 12
            bmi_value = calculate_bmi(weight, feet, inches)
            print("  " + str(round(bmi_value, 1)), end="")
            weight += 10
        print()
        height += 2

def main():
    print("Welcome to the BMI Calculator!")
    print("Type quit at any time to exit.\n")
    keep_running = True
    while keep_running:
        # Get weight
        valid_weight = False
        while not valid_weight:
            weight_input = input("Enter your weight in pounds: ")
            # Quit option
            if weight_input.lower() == "quit":
                print("Exiting program. Goodbye!")
                return
            try:
                weight = float(weight_input)
                if weight <= 0:
                    raise ValueError("Weight must be greater than zero.")
                valid_weight = True
            except Exception as err:
                print("Error:", err)
                print("Please enter a valid weight.\n")
        # Get height in feet
        valid_feet = False
        while not valid_feet:
            feet_input = input("Enter your height (feet): ")
            if feet_input.lower() == "quit":
                print("Exiting program. Goodbye!")
                return
            try:
                height_feet = int(feet_input)
                if height_feet < 0:
                    raise ValueError("Height (feet) cannot be negative.")
                valid_feet = True
            except Exception as err:
                print("Error:", err)
                print("Please enter a valid height in feet.\n")
        # Get height in inches
        valid_inches = False
        while not valid_inches:
            inches_input = input("Enter your height (inches): ")
            if inches_input.lower() == "quit":
                print("Exiting program. Goodbye!")
                return
            try:
                height_inches = int(inches_input)
                if height_inches < 0 or height_inches >= 12:
                    raise ValueError("Height (inches) must be between 0 and 11.")
                valid_inches = True
            except Exception as err:
                print("Error:", err)
                print("Please enter a valid height in inches.\n")
        # Calculate and display results
        bmi = calculate_bmi(weight, height_feet, height_inches)
        category = bmi_category(bmi)
        display_results(bmi, category)
        display_bmi_table()
        # Ask user if they want to run again
        again = input("\nWould you like to calculate another BMI? (yes/no): ")
        # Allow user to quit explicitly
        if again.lower() == "quit":
            print("Exiting program. Goodbye!")
            return
        # Continue only if user types yes
        if again.lower() != "yes":
            keep_running = False
            print("Goodbye!")
main()