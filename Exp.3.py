basesalary = float(input("Enter the employee's base salary:"))
print("Basic Salary:",basesalary)
 
DA = 0.7*basesalary
print("DA(70%):",DA) 
TA = 0.3*basesalary
print("TA(30%):",TA)
HRA = 0.10*basesalary
print("HRA(10%):",HRA)

Grosssalary = DA+TA+HRA
print("grosssalary:",Grosssalary)