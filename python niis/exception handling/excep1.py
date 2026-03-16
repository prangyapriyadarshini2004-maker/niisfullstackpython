print ("main start")
try:
	print(10//0)
	print("try end")
except ZeroDivisionError as e:
	print("caught",e)
	print("d never zero")
print("main end")
