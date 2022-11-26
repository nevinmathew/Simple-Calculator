#This function adds the two numbers
def add(x, y):
    return (x + y)

#This function subtracts the two numbers
def subtract(x, y):
    return (x - y)

#This function multiplies the two numbers
def multiply(x, y):
    return (x * y)

#This function divides the two numbers
def divide(x, y):
    return (x / y)


print("Select operation -> ")
print("1. Add ( + )")
print("2. Subtract ( - )")
print("3. Multiply ( * )")
print("4. Divide ( / )")

while True:
    #Get the input from the user
    choice = input("Enter your choice (1, 2, 3 or 4): ")

    #To check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, " + ", num2, " = ", add(num1, num2))

        elif choice == '2':
            print(num1, " - ", num2, " = ", subtract(num1, num2))

        elif choice == '3':
            print(num1, " * ", num2, " = ", multiply(num1, num2))

        elif choice == '4':
            print(num1, " / ", num2, " = ", divide(num1, num2))
        break
    #Show error if the choice is not one of the four options
    else:
        print("Invalid Input!")
