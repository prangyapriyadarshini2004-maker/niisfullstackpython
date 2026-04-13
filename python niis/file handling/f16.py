import pickle
class Student:
	def __init__(self,roll,name,mark):
		self.roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self.roll,self.name,self.mark)
f=open("student.dat","wb")
s1=Student(101,"Amit",85)
s2=Student(102,"Ravi",90)
s3=Student(103,"Sita",88)
pickle.dump(s1,f)
pickle.dump(s2,f)
pickle.dump(s3,f)
f.close()
