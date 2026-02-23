"""wap take a positive number check no is 2 digit number"""
print("enter a number")
no=int(input())
if no<0:
	n0=-no
	if no>9 and no<100:
		print("2 digit number")