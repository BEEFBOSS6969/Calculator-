import math

# learn how to use user input to do all simple functions
user_input = input("operation:")
if user_input == "add":
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    result = str(num1+num2)
 
if user_input == "subtract":
    num1 = float (input("Enter a number:"))
    num2 = float (input("Enter another number:"))
    result = str(num1-num2)
 
if user_input == "multiply":
    num1 = float (input("Enter a number:"))
    num2 = float (input("enter another number:"))
    result = str(num1*num2)
 
if user_input == "divide":
    num1 = float (input("Enter a number:"))
    num2 = float (input("Enter another number:"))
    result = str(num1/num2)
 
if user_input == "square root":
    num1 = int(input("Enter a number:"))
    result = str(math.sqrt(num1))
 
if user_input == "square":
    num1 = float (input("Enter a number:"))
    result = str(num1*num1)
    
if user_input == "cubing":
    num1 = float (input( "Enter a number:"))
    result = str(num1*num1*num1)
    
if user_input == "exponent":
    num1 = float(input("Enter a number:"))
    num2 = float(input("Enter another number:"))
    result = str(num1**num2)
   
if user_input == "cos":
    num1 = float (input("Enter a number:"))
    result = str(math.cos(num1))
 
if user_input == "sin":
    num1 = float (input("Enter a number:"))
    result = str(math.sin(num1))
 
if user_input == "tan":
    num1 = float (input("Enter a number:"))
    result = str(math.tan(num1))
 
if user_input == "atan":
    num1 = float(input("Enter a number:"))
    result = str(math.atan(num1))
 
if user_input == "acos":
    num1 = float(input("Enter a number:"))
    result = str(math.acos(num1))
 
if user_input == "asin":
    num1 = float(input("Enter a number:"))
    result = str(math.asin(num1))
 
if user_input == "area of a circle":
    radius = float(input("Enter a number:"))
    result = str(radius*radius*3.14)
 
if user_input == "circumference":  
    radius = float(input("Entrer a number:"))
    result = str(2*3.14*radius)
 
if user_input == "area of a rectangle":
    length = float(input("Enter a length:"))
    width = float(input("Enter a width:"))
    result = str(length*Width)
 
if user_input == "perimeter of a recangle":
    length = float(input("Enter a length:"))
    width = float(input("Enter a width:"))
    result = str(length+width+length+width)
 
if user_input == "area of a square":
    length = float(input("Enter a length:"))
    width = float(input("Enter a width:"))
    result = str(length*Width)
 
if user_input == "perimeter of a square": 
    length = float(input("Enter a length:"))
    width = float(input("Enter a width:"))
    result = str(length+length+width+width)
 
if user_input == "area of a parallelogram":
    base = float(input("Enter the width of the parallelogram:"))
    height = float(input("Enter the hieght of the paralleogram:"))
    result = str(base*height)
 
if user_input == "perimeter of a parallelogram":
    base = float(input("Enter the width of the base of the parallelogram:"))
    side = float(input("Enter the legth of the side of the parallelogram:"))
    result = str(2*base+2*base)
 
if user_input == "area of a Rhombus":
    side = float(input("Enter the length of one of the sides of the Rhombus:"))
    height = float(input("Enter the height of the Rhombus:"))
    result = str(side*height)
                
if user_input == "perimeter of a Rhombus":
    side = float(input("Enter the length of one of the sides of the Rhombus:"))
    result =str(side*4)
              
if user_input == "Area of a Trapizoid":
    bottoms_side = float (input("Enter the length of the bottom side of the Trapazoid:"))
    top_side = float (input("Enter the length of the top side of the Trapazoid:"))
    height = float (input("Enter the height of the Trapzoid:"))
    result = str ((bottom_side+top_side)/2(height))
              
if user_input == "Perimeter of a Trapizoid":
    bottom_side = float(input("Enter the length of the bottom side of the Trapazoid:"))
    top_side = float(input("Enter the length of the top side of the Trapizoid:"))
    left_side = float(input("Enter the length of the left side of the Trapizoid:"))
    right_side = float(input("Enter the length of the right side of the Trapizoid:"))
    result = str(bottom_side+top_side+left_side+right_side)
              
if user_input == "Area of a Kite":
    vertical_diagonal = float(input("Enter the distance from the top most vertex of the to the bottom most vertex of the Kite:"))
    horezontal_diagonal =float(input("Enter the distance from the left most vertex to the right most vertex of the KIte:"))
    result = str((vertical_diagonal+horezontal_diagonal)/2)
              
if user_input == "Perimeter of a Kite":
    side_A = float(input("Enter the length of one of the shorter sides of the Kite:"))
    side_B = float(input("Enter the Length of one of the shorter sides of the Kite:"))
    result = str((side_A*2)+(side_B*2))
              
if user_input == "area of a pentagon":
    side = float(input("Enter the length of one of the sides of the pentagon:"))
    radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Pentagon:"))
    result = str((radius*5*side)/2)
              
if user_input == "perimeter of a pentagon":
    side = float(input("Enter the length of one of the sides of the Pentagon:"))
    result = str(side*5)             
              
if user_input == "area of a hexagon":
    side = float(input("Enter the length of one of the sides of the hexagon:"))
    radius = float(input("Enter the distance from the center point of the to the middle point of any side of the sides hexagon:"))              
    result = str((radius*6*side)/2)
              
if user_input == "perimeter of a hexagon":
    side = float(input("Enter the length of one of the sides of the hexagon:"))
    result = str(side*6)
              
if user_input == "area of a heptagon":
    side = float(input("Enter the length of one of sides of the heptagon:"))
    radius = float(input("Enter a the distance fom the center point of the to the middle point of a any side of the heptagon:"))
    result = str((side*radius*7)/2)
              
if user_input == "perimeter of a heptagon":
    side = float(input("Enter the length of one of the sides of the heptagon"))
    result = str(side*7)             
              
if user_input == "perimeter of a octagon":
    side = float(input("Enter the length of one of teh sides of the Octagon:"))
    result = str(side*8)
              
if user_input == "area of a octagon":
    side = float(input("Enter the length of one of the sides of the Octagon:"))
    radius = float(input("Enter the distance from the center point to the middle point of any side of Octagon:"))              
    result = str((side*radius*8)/2)
              
if user_input == " Perimeter of a Nonagon":
    side = float(input("Enter the length of one of the sides of the Nonagon:"))
    result = str(side*9)
              
if user_input == "Area of a Nonagon":
    side = float(input("Enter the length of one of the sides of the Nonagon:"))
    radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Nonagon:"))
    result = str((side*radius*9)/2)
                      
if user_input == "Perimeter of a Decagon":
    side = float(input("Enter the length of one of the sides of the Decagon:"))
    result = str(side*10)
                      
if user_input == "Area of a decagon":
    side = float(input("Enter the length of one of the side of the Decagon:"))
    radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Decagon:"))
    result = str((side*radius*10)/2)             
                      
if user_input == "Perimeter of a Hendecagon":
    side = float(input("Enter the length of one of the sides of the Hendecagon:"))
    result = str(side*11)
                      
if user_input == "Area of a Hendecagon":
    side = float(input("Enter the length of one of the sides of the Hendecagon:"))
    radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Hendecagon:"))
    result = str((side*radius*11)/2)
                      
if user_input == "Perimeter of a Dodecagon":
    side = float(input("Enter the length of one of the sides of the Dodecagon:"))
    result = str(side*12)
                      
if user_input == "Area of a Dodecagon":
    side = float(input("Enter the length of one of the sides of the Dodecagon"))
    radius = float(input("Enter the distance from the center point to the middle point of any of the sides of the Dodecagon"))
    result = str((side*radius*12)/2)

if user_input == "Distance formula":
    x1 = float(input("Enter one of the x values:"))
    x2 = float(input("Enter the other x value:"))
    y1 = float(input("Enter the y value that goes along with the first x value:"))
    y2 = float(input("Enter the other y value:"))
    result = str(math.sqrt(math.sq(x2-x1)+math.sq(y2-y1)))
                      
if user_input == "Volume of a cube":
    side = float(input("Enter the leght of one of the sides of the cube:"))
    result = str(side*side*side)

if user_input == "Volume of a rectangular prism":
    length = float(input("Enter the length of the rectangular prism"))
    width = float(input("Enter the width of the rectangular prism"))
    height = float(input("Enter the height of the rectangular prism"))
    result = str(length*width*heigth)
                         
if user_input == "Volume of a triangular prism":
    base = float(input("Enter the length of the base of the triangular prism:"))
    height = float(input("Enter the height of the triangular prism:"))
    length = float(input("Enter the length of the triangular prism:"))
    result = str((base*hieght*length)/2)
                         
if user_input == "Volume of a pyriamid":
    length = float(input("Enter the length of the bottom of the pyriamid"))
    width = float(input("Enter the width of the bottom of the pyriamid"))
    heigth = float(input("enter the height of the pyrimid:"))
    result = str((length*width*height)/3 
                 
if user_input == "Volume of a cone":
    radius = float(input("Enter the readius of the cone:"))
    height = float(input("Enter the height of the cone:"))
    result = str(math.pie*height(radius*radius)/3)

if user_input == "Volume of a sphere":
    radius = float(input("Enter the radius of the sphere"))
    result = str(4/3*math.pie(radius*radius*radius))
                 
if user_input == "Volume of a cylinder":
    radius = float(input("Enter the radius of the cylinder"))
    height = float(input("Enter the Height of the cylinder"))
    result = str(math.pie*height(radius*radius)           

if user_input == "Pythgoream theorem":
    a = float(input("Enter the value of a:"))
    b = float(input("Enter the value of b:"))
    result = str((a*a)+(b*b))

if user_input == "Quadratic formula":
    b = float(input("Enter the value of b:"))
    a = float(input("Enter the value of a:"))
    c = float(input("Enter the value of c:"))
    result = str(-b+(math.sqrt((b*b)-4*a*c)/2a)
      
if user_input == "Midpoint formula":
    x1 = float(input("Enter the value of x on one of the end of the lines"))
    y1 = float(input("Enter the value of y on the same end of the line that you got the x1 value"))
    x2 = float(input("Enter the value of x on trhe opposite end of the line"))
    y2 = float(input("Enter the value of y on the same end as x2"))
    result = str((x1+x2)/2,(y1+y2))
                 
if user_input == "Slope":
    x1 = float(input("Enter the value of the first x in the equation"))
    y1 = float(input("Enter the value of the first y in the equation"))
    x2 = float(input("Enter the value of the secound x in the equation"))
    y2 = float(input('Enter the value of the secound y in the equation")) 
    result = str((y2-y1),(x2-x1))                                  
 if user_input == "Speed formula physics":
     distance = float(input("Enter the total distance you a going or a object is going:"))
     time = float(input("Enter the total time it takes to travel that distance:"))
     result = str(distance/time)
                     
if user_input == "Time formula physics":
    speed = float(input("Enter the speed at which you or an object is going:"))
    distance = float(input("Enter the total distance you or an object is going"))
    result = str(distance/speed)
                     
if user_input == "Distance formula physics":
    speed = float(input("Enter the speed at which you or an object is going:"))
    time = float(input("Enter the total time spent at that speed:"))
    result = str(speed*time)
                     
if user_input == "Trigonometric formula for sin(2a)":
    a = float(input("Enter the value of a:"))
    result = str(2*math.sin*a*math.cos*a=(2*math.tan*a)/(1+(math.tan*math.tan)*a))

if user_input == "Trigonometric formula for cos(2a)":
    a = float(input("Enter the value of a:"))
    result = str((math.cos*math.cos)a-(math.sin*math.sin)a=2(math.cos*math.cos)a-1)
                     
if user_input == "Trigonometric formula for tan(2a)":
    a = float(input("Enter the vakue of a:'))
    result = str((2*math.tan*a)/(1-(math.tan*math.tan)a)
                 
if user_input== "trigonometric formula for cot(2a)":
    a = float(input("Enter the value of a:"))
    result = str(((math.cot*math.cot)a-1)/(2*math.cot*a))
                   
print (result)
