print("Select Operation:")
print("Add +")
print("Subtract -")
print("Multiply *")
print("Divide /")

operation = input()

if operation == "+":
    number1 = input("Enter Number: ")
    number2 = input("Enter NUmber:")
    print(int(number1) + int(number2))
elif operation == "-":
    number1 = input("Enter Number:")
    number2 = input("Enter Number:")
    print(int(number1) - int(number2))
elif operation == "*":
    number1 = input("Enter Number:")
    number2 = input("Enter Number:")
    print(int(number1) * int(number2))
elif operation == "/":
    number1 = input("Enter Number:")
    number2 = input("Enter Number:")
    print(int(number1) / int(number2))
else:
    print("Error. Choose operation above.")