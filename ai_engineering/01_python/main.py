
def calculate(num1, num2, opt):

    match opt:
        case "+":
            return num1 + num2

        case "-":
            return num1 - num2

        case "*":
            return num1 * num2

        case "/":
            return num1 / num2

        case _:
            raise ValueError("Invalid operation")


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    opt = input("Enter operation: +, -, *, /: ")

    result = calculate(num1, num2, opt)

except ValueError as error:
    print(error)

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("\nResult:", result)

finally:
    print("=== Program End ===")
