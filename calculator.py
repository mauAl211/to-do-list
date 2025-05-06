def calculator (): 
    print("Welcome to the calcualtor")
    num1 = int(input("Enter the first number: "))
    operator = input("Enter the operator (+,-,*,/): ")
    num2 = int(input("Enter the second number: "))
            
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operator"
            
    print("Result:", result)
            
calculator()