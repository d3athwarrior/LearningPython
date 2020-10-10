validChoices: tuple = (1, 2, 3, 4)
while True:
    print("\nSelect operation:")
    print("0. Exit")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = float(input("Enter Choice:"))
    except Exception as ex:
        print("Input error: ", format(ex))
        exit(0)
    else:
        if (choice == 0):
            print("Goodbye!")
            exit(0)
        elif (choice in validChoices):
            try:
                firstNum = float(input("Enter first number: "))
                secondNum = float(input("Enter second number: "))
            except Exception as ex:
                print("Error while parsing the input")
            else:
                if choice == 1:
                    print("Result is:", (firstNum + secondNum))
                elif choice == 2:
                    print("Result is:", (firstNum - secondNum))
                elif choice == 3:
                    print("Result is:", (firstNum * secondNum))
                elif choice == 4:
                    print("Result is:", (firstNum / secondNum))
        else:
            print("Invalid Choice!")
