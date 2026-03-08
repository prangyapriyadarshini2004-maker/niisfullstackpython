def salary(basic):
	hra=basic*0.20
	da=basic*0.40
	return basic+hra+da
basic=float(input("enter basic salary:"))
gross_salary=salary(basic)
print("Gross salary=",gross_salary)