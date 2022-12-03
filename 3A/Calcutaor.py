print("Select operation:")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    #choice = input("Enter choice(+ . - . * . /): ")
    choice = input('Do you want decimal or integers(dec/int):')
    if choice == 'dec':
        choice = input("Enter choice(+ . - . * . /): ")
        if choice in ('+', '-', '*', '/'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '+':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '-':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '*':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '/':
                print(num1, "'/.", num2, "=", divide(num1, num2))
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        
        else:
            print("Invalid Input")
    else:
        choice = input("Enter choice(+ . - . * . /): ")
        if choice in ('+', '-', '*', '/'):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '+':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '-':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '*':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '/':
                print(num1, "'/.", num2, "=", divide(num1, num2))
            
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        
        else:
            print("Invalid Input")


