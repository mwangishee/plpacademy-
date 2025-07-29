num1 = float (input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
op = input("Enter the operation (+, -, *, /):")

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
     result = num1 * num2

elif op == "/":
    if num2 != 0:
      result = num1 // num2

    else:
          result = "Cannot divide by zero:"

    
else:
     result = "Invalid operator"



print("Result:", result)
        
                           

