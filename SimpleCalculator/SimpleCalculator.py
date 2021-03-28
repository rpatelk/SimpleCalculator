def addition(a, b):
    x = a + b
    return x

def subtraction(a, b):
    x = a - b
    return x

def multiplication(a, b):
    x = a * b
    return x

def division(a, b):
    x = a / b
    return x

def main():
    print("Welcome to Simple Calculator!")
    print("This calculator allows you to add, subtract, multiply, and divide.")
    
    firstNum = False
    while firstNum == False:
        num1 = input("Enter first number: ")
        try:
            num1 = float(num1)
        except:
            print("Not a number.")
            continue
        firstNum = True 

    valid = False
    while valid == False:
        print("Operators include: Addition \"+\"; Subtraction \"-\"; Multiplication \"*\"; Division \"/\"; ")
        operator = input("Enter operator: ")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            valid = True
        else:
            print("Not a valid operator.")
            continue

    secondNum = False
    while secondNum == False:
        num2 = input("Enter second number: ")
        try:
            num2 = float(num2)
        except:
            print("Not a number.")
            continue
        secondNum = True 

    answer = 0
    if operator == "+":
        answer = addition(num1, num2)
    elif operator == "-":
        answer = subtraction(num1, num2)
    elif operator == "*":
        answer = multiplication(num1, num2)
    elif operator == "/":
        answer = division(num1, num2)

    print("Answer = ", answer)

if __name__ == "__main__":
    main()