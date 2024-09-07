def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def main():
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = get_operation()
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        print(f"The result of {num1} {operation} {num2} is: {result}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            break

if __name__ == "__main__":
    main()
