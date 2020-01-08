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
 
if user_input == "area of a Rhombus":
 side = float(input("Enter the length of one of the sides of the Rhombus:")
 height = float(input("Enter the height of the Rhombus:")
 result = str(side*height)
 print (result)
                
if user_input == "perimeter of a Rhombus":
 side = float(input("Enter the length of one of the sides of the Rhombus:"))
 result =str(side*4))
 print (result)
              
if user_input == "Area of a Trapizoid":
 bottom side = float(input("Enter the length of teh bottom side of the Trapazoid:"))+
 top side = float(input("Enter the length of the top side of the Trapazoid:"))
 height = float(input("Enter the height of the Trapzoid:"))
 result = str((bottom side+top side)/2(height))
 print (result)
              
if user_input == "Perimeter of a Trapizoid":
 bottom side = float(input("Enter the length of the bottom side of the Trapazoid:"))
 top side = float(input("Enter the length of the top side of the Trapizoid:"))
 left side = float(input("Enter the length of the left side of the Trapizoid:"))
 right side = float(input("Enter the length of the right side of the Trapizoid:"))
 result = str(bottom side+top side+left side+right side)
 print (result)
              
if user_input == "Area of a Kite":
 vertical diagonal = float(input("Enter the distance from the top most vertex of the to the bottom most vertex of the Kite:"))
 horezontal diagonal =float(input("Enter the distance from the left most vertex to the right most vertex of the KIte:"))
 result = str((vertical diagonal+ horezontal diagonal)/2)
 print (result)
              
if user_input == "Perimeter of a Kite":
 side A = float(input("Enter the length of one of the shorter sides of the Kite:"))
 side B = float(input("Enter the Length of one of the shorter sides of the Kite:"))
 result = str((side A*2)+(side B*2))
 print (result)
              
if user_input == "area of a pentagon":
 side = float(input(" Enter the length of one of the sides of the pentagon:")
 radius = int(input("Enter the distance from the center point to the middle point of any of the sides of the Pentagon:"))
 result = str((radius*5*side)/2)
 print (result)
              
if user_input == "perimeter of a pentagon":
 side = float(input("Enter the length of one of the sides of the Pentagon:"))
 result = str(side*5)
 print (result)             
              
if user_input == "area of a hexagon":
 side = float(input("Enter the length of one of the sides of the hexagon:"))
 radius = float(input("Enter the distance from the center point of the to the middle point of any side of the sides hexagon:"))              
 result = str((radius*6*side)/2)
 print (result)
              
if user_input == "perimeter of a hexagon":
 side = float(input("Enter the length of one of the sides of the hexagon:"))
 result = str(side*6)
 print (result)
              
if user_input == "area of a heptagon":
 side = float(input("Enter the length of one of sides of the heptagon:"))
 radius = float(input("Enter a the distance fom the center point of the to the middle point of a any side of the heptagon:"))
 result = str((side*radius*7)/2)
 print (result)
              
if user_input == "perimeter of a heptagon":
 side = float(input("Enter the length of one of the sides of the heptagon")
 result = str(side*7)             
 print (result)
              
if user_input == "perimeter of a octagon":
 side = float(input("Enter the length of one of teh sides of the Octagon:"))
 result = str(side*8)
 print (result)
              
if user_input == "area of a octagon":
 side = float(input("Enter the length of one of the sides of the Octagon:"))
 radius = float(input("Enter the distance from the center point to the middle point of any side of Octagon:"))              
 result = str((side*radius*8)/2)
 print (result)
              
if user_input " Perimeter of a Nonagon":
 side = float(input("Enter the length of one of the sides of the Nonagon:"))
 result = str(side*9)
 print (result)
              
if user_input == "Area of a Nonagon":
 side = float(input("Enter the length of one of the sides of the Nonagon:))
 radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Nonagon:))
 result = str((side*radius*9)/2)                     
 print (result)
                      
if user_input == "Perimeter of a Decagon":
 side = float(input("Enter the length of one of the sides of the Decagon:"))
 result = str(side*10)
 print (result)
                      
if user_input == "Area of a decagon":
 side = float(input("Enter the length of one of the side of the Decagon:"))
 radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Decagon:"))
 result = str((side*radius*10)/2)             
 print (result)
                      
if user_input == "Perimeter of a Hendecagon":
 side = float(input("Enter the length of one of the sides of the Hendecagon:"))
 result = str(side*11)
 print (result)
                      
if user_input == "Area of a Hendecagon":
 side = float(input("Enter the length of one of the sides of the Hendecagon:"))
 radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Hendecagon:"))
 result str((side*radius*11)/2)
 print (result)
                      
if user_input == "Perimeter of a Dodecagon":
 side = float(input("Enter the length of one of the sides of the Dodecagon"))
 result (side*12)
 print (result)
                      
if user_input == "Area of a Dodecagon":
 side = float(input("Enter the length of one of the sides of the Dodecagon"))
 radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Dodecagon"))
 result = str((side*radius*12)/2)
 print (result)
