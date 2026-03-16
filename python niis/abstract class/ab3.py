from abc import ABC, abstractmethod
class Employee(ABC):
	@abstractmethod
	def salary(self):
		pass
class Manager(Employee):
	def salary(self):
		return 50000
class Developer(Employee):
	def salary(self):
		return 40000
class Intern(Employee):
	def salary(self):
		return 15000
e1=Manager()
print(e1.salary())
e2=Developer()
print(e2.salary())
e3=Intern()
print(e3.salary())
