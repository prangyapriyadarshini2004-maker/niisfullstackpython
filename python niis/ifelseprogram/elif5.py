import math
print("Choose a shape to calculate area:")
print("1.Square")
print("2.Rectangle")
print("3.Circle")

choice= int(input("Enter your choice(1-3):"))

if choice ==1:
	side= float(input("Enter the side of the square:"))
	area=side*side
	print("Area of square=",area)

elif choice==2:
	length=float(input("Enter the length of the rectangle:"))
	breadth=float(input("Enter the breadth of the rectangle"))
	area=length*breadth
	print("Area of Rectangle=",area)
elif choice ==3:
	radius= float(input("Enter the radius of the circle"))
	area=math.pi*radius*radius
	print("Area of Circle=",area)

else:
	print("invalid choice")