num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))  
operation=input("Enter operation (+, -, *, /): ")   

if operation == '+':
    result = num1 + num2        
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == '-':      
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")            
elif operation == '*':
    result = num1 * num2    
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")  
