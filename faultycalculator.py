# faulty calculator
# Design a calculator which will correctly solve all the problems except the following ones:
# if the combination of number contain 56 and 9 it will give you 77 as the answer no matter what operation your perform
# same for 45 and 3 , 56 and 6
# Your program should take operator and two numbers as input from the user and then return the result
a = int(input("Enter the first number: "))      # First number input
b = int(input("Enter the second number: "))     # second Number input
# select the operation
print("Please choose the Arithematic operation you want to perform")
c = input(" Press + for addition\n Press - for subtraction\n Press * for multiplication\n Press / for divide\n Your selection is: ")
# faults in the program
if a == 56 and b == 9 or b == 56 and a == 9:    # First Fault
    print("The answer is 77")
elif a == 45 and b == 3 or b == 45 and a == 3:  # Second Fault
    print("The answer is 555")
elif a == 56 and b == 6 or b == 56 and a == 6:  # third fault
    print("The answer is 4")
# correct calculations
elif c == "+":                                  # Addition
    print("The addition is ", a+b)
elif c == "-":                                  # subtraction
    if(a > b):
        print("The subtraction is", a-b)
    else:
        print("ERROR")
elif c == "*":                                  # Multiplication
    print("The Multiplication is", a*b)
elif c == "/":                                  # Division
    print("The division is", a/b)
else:
    # If you have not choosen the operator among the mentioned
    print("Invalid Operator")
