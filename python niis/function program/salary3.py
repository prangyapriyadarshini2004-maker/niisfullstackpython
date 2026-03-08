def salary():
	basic=float(input("enter basic salary:"))
	hra=basic*0.20
	da=basic*0.40
	gross=basic+hra+da
	return gross
gross_salary=salary()
print("Gross salary=",gross_salary)