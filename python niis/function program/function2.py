def add(a,b):
	print("Sum=",a+b)
def sub(a,b):
	print("Difference=",a-b)
def mul(a,b):
	print("Product=",a*b)
def div(a,b):
	if b!=0:
		print("Quotient=",a/b)
	else:
		print("Division by zero not allowed!:")
print("enter two numbers:")
a=int(input())
b=int(input())
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)


