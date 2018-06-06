miles = eval(input("Enter the number of miles: "))
yards = eval(input("Enter the number of yards: "))
feet = eval(input("Enter the number of feet: "))
inches = eval(input("Enter the number of inches: "))
total_inches = 63360*miles+36*yards+12*feet+inches
total_meters = total_inches/39.37
kilometers = int(total_meters/1000)
meters = (total_meters - (kilometers*1000))
centimeters = meters%1
print("Metric length:")
print("{} kilometers".format(int(total_inches/39370)))
print("{} meters".format(int(meters)))
print("{0:.1f} centimeters".format(centimeters*100))
