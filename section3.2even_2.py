#Q26
bagel = eval(input("Q26) Enter number of bagels: "))
if(bagel<6):
    cost=.75*bagel
else:
    cost=.60*bagel
print("{0:} cost is ${1:.2f}".format((4*" "),cost))

#Q28
copy = eval(input("Q28) Enter number of copies: "))
if(copy<=100):
    cost=.05*copy
else:
    cost= 5+.03*(copy-100)
print("{0:} cost is ${1:.2f}".format((4*" "),cost))

#Q30
pay = eval(input("Q30) Enter hourly wage: "))
time = eval(input("{0}Enter number of hours worked: ".format((5*" "))))
if(time<=40):
    wage=time*pay
else:
    wage= (40*pay)+(1.5*pay*(time-40))
print("{0:} Gross pay for week is ${1:.2f}".format((4*" "),wage))

#Q32
word = str(input("Q32) Enter word to translate: "))
word = word.lower()
temp =[]
if (word[0] in ('a','e','i','o','u')):
    word = str(word) + 'way'
    print("     ",word)
else:
    while (word[0] not in ('a','e','i','o','u')) :
        temp.append(word[0])
        word = word.strip(word[0])
    word = str(word[0:]) + str(''.join(temp))+ 'ay'
    print("     ",word)

#34
balance = eval(input("Q34) Enter current balance: "))
widraw = eval(input("     Enter amount of withdrawl: "))
if(widraw<=balance):
    new_balance = balance - widraw
    if(new_balance<150):
        print("     Balance below $150")
    else:
        print("     The new balance is ${0:}".format(new_balance))
else:
    print("     Withdrawal denied.")

#Q36
year = eval(input("Q36) Enter a Year: "))
if(year%100==0):
    if(year%400==0):
        print("{0:}{1:} is a leap year.".format((5*" "),year))
    else:
        print("{0:}{1:} is not a leap year.".format((5*" "),year))
else:
    if(year%4==0):
        print("{0:}{1:} is a leap year.".format((5*" "),year))
    else:
        print("{0:}{1:} is not a leap year.".format((5*" "),year))

#Q38
print("Q38) The four railroad properties are\n     1)Reading\n     2)Pennsylvania\n     3)B & O\n     4)Short Line")
rail = input("     Which is not a railroad? ")
rail=rail.lower()
if(rail=="short line"):
    print("     Correct\n     Short Line is a bus company")
else:
    print("     Wrong\n     Correct answer is Short Line")

#Q40
gpa = eval(input("Q40) Enter your gpa: "))
if(gpa<3.3):
    honors="."
if (3.3<=gpa<3.6):
    honors = " summa cum laude."
if (3.6<=gpa<3.9):
    honors = " magna cum laude."
if ( gpa >=3.9):
    honors = " cum laude."
print("     You graduated" + honors)

#Q42
cost_first = eval(input("Q42) Enter cost of first suit: "))
cost_second = eval(input("     Enter cost of second suit: "))
if(cost_first<=cost_second):
    final_cost = (.50*cost_first)+cost_second
else:
    final_cost = cost_first+(.50*cost_second)
print("     Cost of the two suits is ${0:.2f}".format(final_cost))
