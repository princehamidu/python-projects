print("******")
print("loan simulator")
print("******")

housevalue = float(input("enter the value of the house to be financed: "))
salary = float(input("enter the value of your salary: "))
termyears = int(input("type in how many years you want to pay: "))

deadline1 = termyears * 12
installment = housevalue / (termyears * 12)
approval = (salary * 30)/100

if installment <= approval:
    print("The financed amount to be paid is R${:.2f} per {} months". format(installment,deadline1))
else:
    print("loan denied as it exceeds 30% of your salary" )