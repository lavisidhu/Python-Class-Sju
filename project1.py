Amount = eval(input("Enter amount of change: "))
Quarter = Amount//25
Amount = Amount-(Quarter*25)
Dime = Amount//10
Amount= Amount-(Dime*10)
Nickle = Amount//5
Amount = Amount - (Nickle*5)
Cents = Amount//1
print("Quarters:",Quarter)
print("Dimes :",Dime)
print("Nickles :",Nickle)
print("Cents :",Cents)
