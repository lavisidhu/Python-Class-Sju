loan = eval(input("Enter the amount of loan: "))
rate = eval(input("Enter interest rate(%): "))
time = eval(input("Enter number of years: "))
i=rate/1200
den = 1-(1/(1+i)**(12*time))
payment =(i/den)*loan
print("Monthly payment: ${0:.2f}".format(payment))
