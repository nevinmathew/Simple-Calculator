# Simple Calculator
 A simple calculator using python that can add, subtract, multiply or divide numbers depending upon the input from the user.

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


 print("Select your operation -> ")
 print("Enter 1 for addition (+)")
 print("Enter 2 for subtraction (-)")
 print("Enter 3 for multiplication (*)")
 print("Enter 4 for division (/)")

 while True:
     #Get the input from the user
     choice = input("Enter your choice (1, 2, 3 or 4): ")

     #To check if the choice is one of the four options
     if choice in ('1', '2', '3', '4'):
         num1 = float(input("Please enter the first number: "))
         num2 = float(input("Please enter the second number: "))

         if choice == '1':
             print(num1, " + ", num2, " = ", add(num1, num2))

         elif choice == '2':
             print(num1, " - ", num2, " = ", subtract(num1, num2))

         elif choice == '3':
             print(num1, " * ", num2, " = ", multiply(num1, num2))

         elif choice == '4':
             print(num1, " / ", num2, " = ", divide(num1, num2))
         break #To exit the while True loop

     #Show error if the choice is not one of the four options
     else:
         print("Invalid Input!")
