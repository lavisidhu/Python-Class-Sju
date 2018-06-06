gpa = 3.49
result = ""
if gpa >= 3.5:
    result = "Honors"
print("Q2)" + " " + result + "Student")
print("Q4)" + " " + str('A' < 'B' < 'c'))
change = 356
if change >= 100:
    print("Q6)" + " " + "Your change contains", change // 100, "dollars.")
else:
    print("Q6)" + " " + "Your change contains no dollars.")
length = eval(input("Q8) Enter length of cloth in yards: "))
if length < 1:
    cost = 3.00 # cost in dollars
else:
    cost = 3.00 + ((length - 1) * 2.50)
result = "Cost of cloth is ${0:0.2f}.".format(cost)
print("    " + result)
isvowel = False
letter = input("Q10) Enter a letter: ")
letter = letter.upper()
if (letter in "AEIOU"):
    isvowel = True
if isvowel:
    print("     " + letter, "is a vowel.")
elif (not(65 <= ord(letter) <= 90)):
    print("     " + "You did not enter a letter.")
else:
    print("     " + letter, "is not a vowel.")
number = 5
if number < 0:
    print("Q12)" + " " + "negative")
else:
    if number == 0:
        print("Q12)" + " " + "zero")
    else:
        print("Q12)" + " " + "positive")
if "":
    print("Q14)" + " " + "An empty string is true.")
else:
    print("Q14)" + " " + "An empty string is false.")
print("Q16) Error in if condition \n     Correct Code:\n     number =6\n     if 5<number<9:\n"\
    "       print('Yes')\n     else:\n      print('No')")
print("Q18) Error: Assignment operator is used instead of comparasion operator\n     Correct Code:")
print("     if a==b:\n      print('same')")
