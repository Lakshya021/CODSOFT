a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
while True:
    c = int(input("\nPress 1 for add\nPress 2 for subtract\nPress 3 for multiplication\nPress 4 for division\nPress 5 for exit\n\n"))
    if (c == 1):
        print("\n",a + b)
    elif (c == 2):
        print("\n",a - b)
    elif (c == 3):
        print("\n",a * b)
    elif (c == 4):
        print("\n",a / b)
    elif (c == 5):
        print("Calculator exited successfully.")
        break
    else:
        print("\nInvalid input")