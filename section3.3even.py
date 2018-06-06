num = 3
while num < 15:
    num += 5
print("Q2)" + " " + str(num))
total = 0
num = 1
while num < 5:
    total += num
    num += 1
print("Q4)" + " " + str(total))
oceans = ["Atlantic", "Pacific", "Indian", "Arctic", "Antarctic"]
i = len(oceans) - 1
while i >= 0:
    if len(oceans[i]) < 7:
        del oceans[i]
    i = i - 1
print("Q6)" + " " + str(", ".join(oceans)))
numTries = 0
year = 0
while (numTries < 7) and (year != 1964):
    numTries += 1
    year = int(input( "Q8)" + "Try #" + str(numTries) + ": In what year " +
"did the Beatles invade the U.S.? "))
    if year == 1964:
        print("\nYes. They performed on the Ed Sullivan show in 1964.")
        print("You answered correctly in " + str(numTries) + " tries.")
    elif year < 1964:
        print("Later than", year)
    else: # year > 1964
        print("Earlier than", year)
    if (numTries == 7) and (year != 1964):
        print("\nYour 7 tries are up. The answer is 1964.")
