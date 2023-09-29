def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero isn't possible")
    return x / y

def calculator():
    print("Welcome to Nixon's Calculator")
    
    user_name = input("Please enter your name: ")
    registration_number = input("Please input your Registration number: ")
    print(f"Hello, {user_name}! (Registration Number: {registration_number})")

    while True:
        try:
            print("\nSelect operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Quit")

            choice = int(input("Enter choice (1/2/3/4/5): "))

            if choice == 5:
                print("You're leaving the calculator. Goodbye!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Try again and choose a valid option.")
                continue
            
            num1 = float(input("Input your first number: "))
            num2 = float(input("Input your second number: "))

            if choice == 1:
                result = add(num1, num2)
                operator = "+"
            elif choice == 2:
                result = subtract(num1, num2)
                operator = "-"
            elif choice == 3:
                result = multiply(num1, num2)
                operator = "*"
            elif choice == 4:
                try:
                    result = divide(num1, num2)
                    operator = "/"
                except ValueError as e:
                    print(e)
                    continue

            print(f"{num1} {operator} {num2} = {result:.2f}")

        except ValueError as e:
            print(e)
            continue
        except Exception as e:
            print(f"Error detected in your code: {e}")
            continue

if __name__ == "__main__":
    calculator()