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
    print(f"You are classified as: {category}")
    print("\nBMI Legend, according to the World Health Organization (WHO):")
    print("Underweight: Less than 18.5")
    print("Normal weight: 18.5 - 24.9")
    print("Overweight: 25 - 29.9")
    print("Obese: 30 and above")

def main():
    print("Welcome to the BMI Calculator!")
    try:
        # Validate input type and range
        weight = float(input("Enter your weight in pounds: "))
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        height_feet = int(input("Enter your height (feet): "))
        if height_feet < 0:
            raise ValueError("Height (feet) cannot be negative.")
        height_inches = int(input("Enter your height (inches): "))
        if not (0 <= height_inches < 12):
            raise ValueError("Height (inches) must be between 0 and 11.")
        # Perform calculations
        bmi = calculate_bmi(weight, height_feet, height_inches)
        category = bmi_category(bmi)
        # Output results
        display_results(bmi, category)
    # 2. Catch any exceptions during input validation
    except Exception as err:
        print(f"\nError: {err}")
        print("Program terminated due to invalid input.")
main()