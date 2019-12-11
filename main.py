import math

user_input = input("operation:")
if user_input == "add":
 num1 = float(input("Enter a number:"))
 num2 = float(input("Enter another number:"))
 result = str(num1+num2)
 print (" the answer is"+ result)
if user_input == "subtract":
 num1 = float (input("Enter a number:"))
 num2 = float (input("Enter another number:"))
 result = str(num1-num2)
 print (" the answer is" + result)
if user_input == "multiply":
 num1 = float (input("Enter a number:"))
 num2 = float (input("enter another number:"))
 result = str(num1*num2)
 print (" the answer is" + result)
if user_input == "divide":
 num1 = float (input("Enter a number:"))
 num2 = float (input("Enter another number:"))
 result = str(num1/num2)
 print (" the answer is" + result)
if user_input == "square root":
 num1 = float (input("Enter a number:"))
 result = str(math.sqrt(num1))
 print ("the answer is" + result)
if user_input == "square":
 num1 = float (input("Enter a number:"))
 result = str(num1*num1)
 print ("the answer is" + result)
if user_input == "cos":
 num1 = float (input("Enter a number:"))
 result = str(math.cos(num1))
 print ("the answer is" + result)
if user_input == "sin":
 num1 = float (input("Enter a number:"))
 result = str(math.sin(num1))
 print ("the answer is " + result)
if user_input == "tan":
 num1 = float (input("Enter a number:"))
 result = str(math.tan(num1))
 print ("the answer is " + result)
if user_input == "cubing":
 num1 = float (input( "Enter a number:"))
 result = str(num1*num1*num1)
 print (" the answer is " + result)
if user_input == "exponent":
 num1 = float ( input( "Enter a number:"))
 num2 = float ( input( "Enter another number:"))
 result = str(num1^num2)
 print (" The answer is " + result)
