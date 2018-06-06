# Q68
PurchasePrice = eval(input("Q68 Enter the Purchase Price "))
SellingPrice = eval(input("    Enter the Selling Price "))
if PurchasePrice<SellingPrice:
    PercentProfit = ((SellingPrice-PurchasePrice)/PurchasePrice)/100
    print("{} {}{}".format("    Percent Profit is ", PercentProfit,"%"))
else:
    print("    There is a Loss!!!")

# Q69
Production = int(18) # corn production per acre
Total_Land = int(30) # land in acre
Total_Production = Production*Total_Land
print("{} {} {} {} {}".format("Q69 Production on ",Total_Land,"acre land is",Total_Production,"tons"))

# Q72
Start_Mile = 23352 # Start reading of odometer
End_Mile = 23695 # end reading of odometer
Gas_Consumption = 14 # No. of gallons used
Mileage = (End_Mile - Start_Mile)/Gas_Consumption
print("Q72 Car can run {0:.2f} miles per gallon".format(Mileage))

# Q73
Average_Consumption = 1600 # water consumption per day per person
Population = 315000000
Total_Consumption = Average_Consumption*Population*365 # Consumption for 365 days( 1 year)
print("Q73 Total water consumption in United States is {0:.0f} million gallons per year".format(Total_Consumption/1000000)) # converted to millions

# Q77
National_Debt = (1.68*10**13)
Us_Population = (3.1588*10**8)
Percapita_debt = (National_Debt//Us_Population)
print("Q77 Per capita U.S national debt is ${0:.2f}".format(Percapita_debt))

# Q78
Feet_in_Mile = 5280 # no. of feet in one mile
Calories_Cubic_Foot = 48600 # calories in one cubic foot
Calories_cubic_mile = Feet_in_Mile * Calories_Cubic_Foot
print("Q78 There are {} calories in one cubic mile".format(Calories_cubic_mile))
