print("simple calculator")

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

print (" press 1 for addition \n press 2 for substration \n press 3 for multiplication \n press 4 for division")

choice = int(input("enter your choice from 1-4:"))

if choice == 1:
    print ("Addition of given two number is",num1 + num2)
elif choice == 2:
    print ("subtraction of given two number is",num1 - num2)
elif choice == 3:
    print ("Multiplication of given two number is",num1 * num2)
elif choice == 4:
    print ("Division of given two number is",num1 / num2)
else:
    print ("Invalid input")
