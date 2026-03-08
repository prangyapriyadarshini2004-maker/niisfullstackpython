def salary(basic):
	hra=basic*0.20
	da=basic*0.40
	gross=basic+hra+da
	print("Basic salary=",basic)
	print("HRA=",hra)
	print("DA=",da)
	print("Gross salary=",gross)
basic=float(input("enter basic salary:"))
salary(basic)
