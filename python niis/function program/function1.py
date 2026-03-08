def add():
	print("enter two numbers:")
	a=int(input())
    b=int(input())
	print("Sum=",a+b)
def sub():
	print("enter two numbers:")
	a=int(input())
	b=int(input())
	print("Difference=",a-b)
def mult():
	print("enter two numbers:")
	a=int(input())
	b=int(input())
	print("Product=",a*b)
def div():
	print("enter two numbers:")
	a=int(input())
	b=int(input())
	if b!=0:
		print("Quotient=",a/b)
	else:
		print("Division by zero not allowed")
add()
sub()
mult()
div()
	
