while True:
    print("\n--- Simple Calculator ---")
    print("Operations: +  -  *  /")
    print("Type 'q' to exit.")

    operation = input("Enter operation: ")

    if operation.lower() == "q":
        print("Calculator closed.")
        break

    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Please try again.")
        continue

    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    else:  # Division
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = first_number / second_number

    print(f"Result: {result}")
