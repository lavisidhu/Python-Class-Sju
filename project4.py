price = eval(input("Enter price of item: "))
print("Enter weight of item in pounds and ounces separately.")
pound = eval(input("Enter pounds: "))
ounces = eval(input("Enter ounces: "))
p_oun = pound*16
t_oun = ounces+p_oun
price_oun = price/t_oun
print("Price per ounces: ${0:.2f}".format(price_oun))
