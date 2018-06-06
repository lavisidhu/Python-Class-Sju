while True:
    loan = (input("Q1) Enter the amount of the loan: "))
    if(loan.replace('.','').isdigit()):
        loan=float(loan)
        break
    else:
        print("enter valid value")
        continue
while True:
    interst = (input(" Enter the interest rate: "))
    if(interst.replace('.','').isdigit()):
        interst=float(interst)
        break
    else:
        print("enter valid value")
        continue
while True:
    time = (input(" Enter the duration in months: "))
    if(time.isdigit()):
        time=int(time)
        break
    else:
        print("enter valid value")
        continue
payment = ((loan*(interst/1200))/(1-(1+(interst/1200))**(-1*time)))
total_int = (time*(payment))-loan
print("Monthly Payment: ${0:.2f}".format(payment))
print("Total interest paid: ${0:,.2f}".format(total_int))
