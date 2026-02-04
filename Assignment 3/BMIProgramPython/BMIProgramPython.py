# Create a program that asks users for their weight in pounds and their height in feet and inches. 
# Calculate and display their BMI. Format the output to one decimal place. Include a legend that 
# displays value ranges for underweight, normal, and overweight.
# Body mass index formula (Wikipedia): weight / height^2 * 703
# Expressed in units of lbs/in^2
def calculate_bmi(weight_pounds, height_feet, height_inches):
    # Convert height to total inches
    total_height_inches = (height_feet * 12) + height_inches
    # Calculate BMI using the formula
    bmi = (weight_pounds / (total_height_inches ** 2)) * 703
    return bmi
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    else:
        return "Overweight"
def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in pounds: "))
    height_feet = int(input("Enter your height (feet): "))
    height_inches = int(input("Enter your height (inches): "))
    bmi = calculate_bmi(weight, height_feet, height_inches)
    category = bmi_category(bmi)
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"You are classified as: {category}")
    print("\nBMI Legend, according to the World Health Organization (WHO):")
    print("Underweight: Less than 18.5")
    print("Normal weight: 18.5 - 24.9")
    print("Overweight: 25 - 29.9")
    print("Obese: 30 and above")
main()