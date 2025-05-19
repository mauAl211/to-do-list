def calculator (): 
    print("Welcome to the calcualtor")
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            print("You entered: ", num1)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        operator = input("Enter the operator (+,-,*,/): ")
        print("You entered: ", operator)
        if operator not in ["+", "-", "/", "*"]:
          print("Invalid input. Please enter one of the following '+, -, /, *")
          continue
          
        try:
            num2 = int(input("Enter the second number: "))
            print("you entered: ",num2)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

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
                 print("Error: Division by zero")
        else:
            result = "Invalid operator"
            
        print(f"{num1} {operator} {num2} = {result}")
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower()== "no":
            print("Goodbye monsieur!")
            break  

calculator()