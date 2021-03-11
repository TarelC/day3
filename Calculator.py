print("Select Operation:")
print("Add A")
print("Subtract S")
print("Multiply X")
print("Divide /")

operation = input()

if operation == "A":
    number1 = input("Enter Number: ")
    number2 = input("Enter NUmber:")
    print(int(number1) + int(number2))
elif operation == "S":
    number1 = input("Enter Number:")
    number2 = input("Enter Number:")
    print(int(number1) - int(number2))
elif operation == "X":
    number1 = input("Enter Number:")
    number2 = input("Enter Number:")
    print(int(number1) * int(number2))
elif operation == "/":
    number1 = input("Enter Number:")
    number2 = input("Enter Number:")
    print(int(number1) / int(number2))
else:
    print("Error. Choose operation above.")