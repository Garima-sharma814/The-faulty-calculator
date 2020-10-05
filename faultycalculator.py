# faulty calculator
a = int(input("enter the no."))
b = int(input("enter the no."))
print("the calculation you want to perform")
c = input("press + for addition\n press - for subtraction\n press * for multiplication\n press / for divide\n your selection is ")
if a == 56 and b == 9 or b == 56 and a == 9:
    print("77")
elif c == "+":
    print(a+b)

elif c == "-":
    if(a > b):
        print(a-b)
    else:
        print("error")
elif a == 45 and b == 3 or b == 45 and a == 3:
    print("555")
elif c == "*":
    print(a*b)

elif a == 56 and b == 6 or b == 56 and a == 6:
    print("4")
elif c == "/":
    print(a/b)
else:
    print("invalid operator")
