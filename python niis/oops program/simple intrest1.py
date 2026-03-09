class Simple:
	def __init__(self,p,r,t):
		self.p=p
		self.rate=r
		self.time=t
	def show(self):
		print("principle=",self.p)
		print("rate=",self.rate)
		print("time=",self.time)
	def sical(self):
		return self.p*self.rate*self.time/100
i1=Simple(1000,10,2)
i1.show()
print("Simple intrest=",i1.sical())
