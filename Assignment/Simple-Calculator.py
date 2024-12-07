def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error,division by 0"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error,division by 0"
    return a % b


print("Select operation:\n"
      "1.Add\n"
      "2.Subtract\n"
      "3.Multiply\n"
      "4.Divide\n"
      "5.Modulus")

try:
    user_input = int(input("Enter choice(1/2/3/4/5):"))
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if user_input == 1:
        result = addition(a, b)
        print(f"{a} + {b} = {result}")
    elif user_input == 2:
        result = subtraction(a, b)
        print(f"{a} - {b} = {result}")
    elif user_input == 3:
        result = multiplication(a, b)
        print(f"{a} * {b} = {result}")
    elif user_input == 4:
        result = division(a, b)
        print(f"{a} / {b} = {result}")
    elif user_input == 5:
        result = modulus(a, b)
        print(f"{a} % {b} = {result}")
    else:
        print("Invalid choice")

except ValueError:
    print("Invalid input,Please enter numeric values")
