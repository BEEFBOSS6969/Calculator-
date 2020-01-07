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
 num1 = int(input("Enter a number:"))
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
 num1 = float(input("Enter a number:"))
 num2 = float(input("Enter another number:"))
 result = str(num1**num2)
 print (" The answer is " + result)
if user_input == "atan":
 num1 = float(input("Enter a number:"))
 result = str(math.atan(num1))
 print (" The answer is " + result)
if  user_input == "acos":
 num1 = float(input("Enter a number:"))
 result = str(math.acos(num1))
 print ("the answer is" + result)
if user_input == "asin":
 num1 = float(input("Enter a number:"))
 result = str(math.asin(num1))
 print ("the answer is" + result)
if user_input == "area of a circle":
 radius = float(input("Enter a number:"))
 result = str(radius*radius*3.14)
 print ("the answer is" + result)
if user_input == "circumference":  
 radius = float(input("Entrer a number:"))
 result = str(2*3.14*radius)
 print ("the answer is" + result)
if user_input == "area of a rectangle":
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length*Width)
 print ("The area of the rectangle is:" + result)
if user_input == "perimeter of a recangle":
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length+width+length+width)
 print ("The primeter of a rectangle is:" + result)
if user_input == "area of a square":
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length*Width)
 print ("The area of the square is:" + result)
if user_input == "perimeter of a square": 
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length+length+width+width)
 print (" the perimeter of the square is:" + result)                                          
if user_input == "area of a parallelogram":
 base = float(input("Enter the width of the parallelogram:"))
 height = float(input("Enter the hieght of the paralleogram:"))
 result = str(base*height)
 print ("The area of the parallelogram is:" + result)
if user_input == "perimeter of a parallelogram":
 base = float(input("Enter the width of the base of the parallelogram:"))
 side = float(input("Enter the legth of the side of the parallelogram:"))
 result = str(2*base+2*base)
 print ("The perimeter of the parallelogram is:" + result)              
# put the start of the area of a pentagon a function here once you figure it out
if user_input == "perimeter of a pentagon":
 side = float(input("Enter the length of one of the sides of the Pentagon:"))
 result = str(side*5)
 print ("The perimeter of the Pentagon is" + result)             
if user_input == "area of a hexagon":
 side = int(input("Enter the length of one of the sides of the hexagon:"))
 result = str(math.sqrt(3)(3)/2(side*side))
if user_input = " area of a hexagon2.0":
  side = int(input("Enter the length of one of the sides of the hexagon:"))
  radius = int(input("Enter the distance from the center of the hexagon to the middle point of one of the sides:") 
  result = str(6*(side*radius))  
print (result)
 print ("The area of the Hexagon is:" + result)
if user_input == "perimeter of a hexagon":
 side = float(input("Enter the length of one of the sides of the hexagon:"))
 result = str(side*6)
 print ("The perimeter of the Hexagon is:" + result)
if user_input == "area of a heptagon":
 perimeter = float(input(" Enter the perimeter of the heptagon:"))
 apothem = float(input("Enter a the distance fom the middle of the heptagon to the middle of a any side:"))
 result = str((perimeter*apothem)/2)
 print (" The area of the heptagon is" + result)
if user_input == "perimeter of a heptagon":
 side = float(input("Enter the length of one of the sides of the heptagon"))
 result = str(side*6)
 print (" The perimeter of the Heptagon is:" + result)
if user_input == "perimeter of a octagon":
 side = float(input("Enter the length of one of teh sides of the Octagon:"))
 result = str(side*8)
 print ("The perimeter of the octagon is:" + result)
if user_input == "area of a octagon":
 side = float(input("Enter the length of one of the sides of the octagon:"))
 result = str(2(1+math.sqrt(2)side*side)
 print (" The area of the octagon is:" + result)
