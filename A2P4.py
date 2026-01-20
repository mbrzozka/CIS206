# Allow a use to enter two floating point numerical values. Display the 
# product of the two numbers.
def main():
    num1 = float(input("Enter the first floating point number: "))
    num2 = float(input("Enter the second floating point number: "))
    product = num1 * num2
    print("The product of", num1, "and", num2, "is:", product)
main()