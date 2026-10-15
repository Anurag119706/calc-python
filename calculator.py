import math

def add(a,b):
    result = b
    count = 0
    while count < a:
        result = result - (-1)
        count = count - (-1)
    return result

def subtract(a,b):
    result = a
    count = 0
    while count < b:
        result = result + (-1)
        count = count + 1
    return result

def multiply(a,b):
    if b:
        return a + multiply(a, b - 1)
    else:
        return 0

def divide(a,b):
    if b:
        if a < b:
            return 0
        else:
            return 1 + divide(a - b, b)
    else:
        return "Error, Division by zero is not allowed"

def floor_divide(a,b):
    if b:
        if a < b:
            return 0
        else:
            return 1 + floor_divide(a - b, b)
    else:
        return "Error, Division by zero is not allowed"

def modulus(a,b):
    if b:
        return a % b
    else:
        return modulus(a - b, b)

def display_menu():
    print("-------- CALCULATOR MENU --------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exit")
    print("----------------------------------")

def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    display_menu()
    choice = input("Enter your choice (1-7):").strip()

    if choice in "1":
        print("\nResult: ",add(a,b))

    elif choice in "2":
        print("\nResult: ",subtract(a,b))

    elif choice in "3":
        print("\nResult: ",multiply(a,b))

    elif choice in "4":
        print("\nResult: ",divide(a,b))

    elif choice in "5":
        print("\nResult: ",floor_divide(a,b))

    elif choice in "6":
        print("\nResult: ",modulus(a,b))

    elif choice in "7":
        print("Thank you")
        return

    elif choice in "_":
        print("Invalid choice. Please choose between 1 to 7")

    else:
        print("Invalid choice. Try again")

if __name__ == "__main__":
    calculator()