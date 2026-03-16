class Demo:
	def __init__(self,n):
		self.n=n
		print("constructor",self.n)
	def __del__(self):
		print("destructor",self.n)
d1=Demo("first")
print(id(d1))
d2=Demo("second")
d3=Demo("third")