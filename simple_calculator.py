def calculator():
    print("simple calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")
    
num1 = float(input("input first number"))
num2 = float(input("input second number"))
operation = input("enter operation (+, -, *, /)")
#results 
if operation == "+":
    result = num1 + num2 
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1/num2 


#print the results
print(f"result: {num1}{operation}{num2} = {result}")


