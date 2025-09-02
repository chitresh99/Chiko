print("Simple Python Calculator")
print("Supported operations: +, -, *, /")

while True:
    try:
        a = float(input("\nEnter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
            if b == 0:
                print("Error: Division by zero not allowed!")
                continue
        else:
            print("Invalid operation entered. Please try again.")
            continue

        print(f"\nResult: {a} {op} {b} = {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero encountered.")

    choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if choice != 'yes':
        print("\nGoodbye!")
        break