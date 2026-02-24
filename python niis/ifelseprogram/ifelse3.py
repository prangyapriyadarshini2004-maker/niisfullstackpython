#wap take a person's age from keyboard check person is eligible for voting or not
print("enter a age")
age=int(input())
#print("eligible") if age>=18 else print("not eligible")
msg="eligible" if age>=18 else "not eligible"
print(msg)
