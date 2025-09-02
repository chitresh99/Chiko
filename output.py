print("Simple Calculator")
print("Type 'quit' to exit\n")

while True:
    num1 = input("Enter first number: ")
    if num1 == 'quit':
        break
    num2 = input("Enter second number: ")
    if num2 == 'quit':
        break
    operator = input("Enter operator (+, -, *, /): ")
    if operator == 'quit':
        break

    try:
         result = float(num1) + float(num2) if operator == '+' else \
              float(num1) - float(num2) if operator == '-' else \
              float(num1) * float(num2) if operator == '*' else \
              (float(num1) / float(num2)) if operator == '/' else None
        if result is None or operator not in "+-*/":
            print("Invalid operator or division by zero.\n")
            continue
        print(f"Result: {result}\n")
    except ValueError:
        print("Please enter valid numbers.\n")
    except ZeroDivisionError:
        print("Cannot divide by zero.\n")