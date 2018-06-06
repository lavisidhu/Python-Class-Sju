# Q97
Lght_Thun=eval(input("Q97 Enter number of seconds between lightning and thunder: "))
Dist_Storm=Lght_Thun/5
print("    Distance from storm: {0:.2f} miles.\n".format(Dist_Storm))

# Q100
Watt = eval(input("Q100 Enter wattage of device: "))
Hour = eval(input("     Enter number of hours used: "))
Price = eval(input("     Enter price per KWh in cents: "))
Cost = (Watt*Hour)/(1000*Price)
print("     Cost of electricity: ${0:.2f} \n".format(Cost))

# Q102
Earning = eval(input("Q102 Enter earnings per share: "))
Price_Share = eval(input("     Enter price per share: "))
Ratio = Price_Share/Earning
print("     Price-to-Earning ratio: {0:.2f} \n".format(Ratio))

# Q107
Tax_Bracket = eval(input("Q107 Enter tax bracket(as decimal): "))
Int_Rate = eval(input("     Enter municipal bond interest rate(as %): "))
Cd_Rate = Int_Rate/(1-Tax_Bracket)
print("     Equivalent CD interest rate: {0:.3f}% \n".format(Cd_Rate))

# Q110
Str1=input("Q110 Enter a sentence: ")
Old = input("     Enter word to replace: ")
New = input("     Enter replacement word: ")
Str1 = Str1.replace(Old,New)
print("    ",Str1,"\n")

# Q111
Time = int(input("Q111 Enter number of months: "))
Year = Time//12
Months = Time%12
print("     {0} months is {1} years and {2} months.".format(Time,Year,Months))
