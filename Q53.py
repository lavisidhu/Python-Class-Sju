# Q53
Bill = eval(input("Q53 Enter amount of bill: "))
Per_Tip = eval(input("    Enter percentage of tip: "))
Tip = (Per_Tip*Bill)/100
print("    Tip: ${0:.2f}\n".format(Tip))

# Q55
Salary = eval(input("Q55 Enter the salary: "))
Inc_Salary = 1.10*Salary
Dec_Salary = 0.90*Inc_Salary
Per_change = ((Dec_Salary - Salary)/Salary)
print("    New salary: ${0:,.2f}".format(Dec_Salary))
print("    Change: {0:.2%}\n".format(Per_change))

# Q57
Principal = eval(input("Q57 Enter principal: "))
Int_rt = eval(input("    Enter interest rate (as %): "))
Year = eval(input("    Enter number of years: "))
Amount = Principal*(1+Int_rt/100)**Year
print("    Future value: ${0:,.2f}\n".format(Amount))

# Q58
Future_value = eval(input("Q58 Enter future value: "))
Int_Rate = eval(input("    Enter interest rate (as %): "))
Period = eval(input("    Enter number of years: "))
Present_Value = Future_value/(1+Int_Rate/100)**Period
print("    Present value: ${0:,.2f}".format(Present_Value))
