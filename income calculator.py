print("CALCULATE YOUR SALARY")
b=int(input("PLEASE ENETR YOUR BASIC PAY="))
print("BASIC PAY=",b)
gross=b*0.033334
print("GROSS INCOME(per day)=",gross)
print("HRA=10% of BASIC PAY")
hra=b*0.1
print("HRA OF YOUR INCOME=",hra)
ta=b*0.05
print("TA=5% of BASIC PAY")
print("TA=",ta)
prf=b*0.02
print("PROFESSIONAL TAX=2% OF YOUR BASIC PAY")
print("PROFESSIONAL TAX=",prf)
netsalary=b-hra-ta-prf
print("NET.SALARY=",netsalary)

