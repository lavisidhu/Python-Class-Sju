list = []
bond = ['SPY','QQQ','EEM','VXX']
for i in range(len(bond)):
    x = input("enter the valu of {}: ".format(bond[i]))
    list.append(float(x))
print("{0:10s} {1:>10s}".format("ETF","PERCENTAGE"))
print('-'*22)
for i in range(len(bond)):
    print("{0:10s} {1:>10,.2%}".format(bond[i],list[i]/sum(list)))
print("\nTOTAL AMOUNT INVESTED: ${0:,.2f}".format(sum(list)))
