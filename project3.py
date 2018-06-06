fvalue = eval(input("Enter face value of bond: "))
rate = eval(input("Enter coupn interest rate(%): "))
time = eval(input("Enter years until maturity: "))
mprice = eval(input("Enter market price of bond: "))
intr = (rate*fvalue)/100
a = (fvalue - mprice)/time
b = (fvalue+mprice)/2
ytm = (intr+a)/b
print("Approximate YTM: {0:.2%}".format(ytm))
