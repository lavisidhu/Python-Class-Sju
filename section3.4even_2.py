# #Q52
# phone = input("Q52 Enter a telephone number: ")
# phone = phone.replace("-",'')
# print("    Number without dashes is ",phone)
#
# #Q54
# num1 = input("Q54) Enter number1: ")
# num2 = input("     Enter number2: ")
# num3 = input("     Enter number3: ")
# if(num1>num2):
#     if(num1>num3):
#         print("     Largest number: ",num1)
# else:
#     if(num2>num3):
#         print("     Largest number: ",num2)
#     else:
#         print("     Largest number:",num3)
#
# #Q56
# sum=0
# for i in range(101):
#     sum = sum+i
# print("Q56) The sum 1+2+3+......+100 is ",sum)
#
# #58
# word = input("Q58) Enter a word: ")
# vowel = ['a','e','i','o','u']
# check = 1
# for i in range(5):
#     if(vowel[i] not in word):
#         check = 0
#         break
# if(check==1):
#     print("     {} is a vowel word".format(word.upper()))
# else:
#     print("     {} is not a vowel word".format(word.upper()))
#
# #60
# investment = 1000
# int_rate = .05
# time = 4
# interest = 0
# compound = 0
# print("Q60)  {0:13s} {1:>13s}".format("Simple Interest","Compound Interest"))
# for i in range(1,5):
#     interest = (i*50)
#     compound =compound+50+(int_rate*compound)
#     # print("{} ${}".format(i,(investment+interest)))
#     # print("{} ${}".format(i,(investment+compound)))
#     print("     {0} ${1:,.2f} {2:>10s}{3:,.2f}".format(i,float(investment+interest),"$",float(investment+compound)))
#
# #62
# deposit = 100
# interst = .03
# balance = 0
# print("Q62) {0:10s} {1:>10s}".format("Year","Balance"))
# for i in range (2014,2019):
#     for j in range(12):
#         balance=balance+((interst/12)*balance)+deposit
#     print("     {0:}{1:>10s}{2:,.2f}".format(i,'$',float(balance)))
#
# #Q64
# price = 20000
# depr = .15
# balance = price
# print("Q64) {0:10s} {1:>10s}".format("Year","Depr_price"))
# for i in range (1,5):
#     balance=balance-(depr*balance)
#     print("     {0:3}{1:>9s}{2:,.2f}".format(i,'$',float(balance)))
#
# #66
# number = eval(input("Q66) How many numbers do you want to enter? "))
# mylist =[]
# m = number//2
# for i in range(1,number+1):
#     num=input("     Enter Number{}: ".format(i))
#     mylist.append(num)
#     mylist.sort()
# if(number%2!=0):
#     result=(float(mylist[m]))
# else:
#     result=float((float(mylist[m-1])+float(mylist[m]))/2)
# print("     Median: ",result)
#
# #68
# stock = 10000
# temp = stock
# for i in range(1,7):
#     temp=temp-(.16*temp)
# # temp1 = temp
# for i in range(1,7):
#     temp=temp+(.18*temp)
# print("Q68) The value of the stock at the\nend of the year was ${0:.2f}".format(temp))
#
# #70
# infile = open('SBWinners.txt','r')
# winners=[]
# for line in infile:
#     line = line.rstrip()
#     line = line.lower()
#     winners.append(line)
# infile.close
# win=winners.index('steelers')+1
# print("Q70) The steelers first won the Super Bowl in game #{}.".format(win))

#Q72
my_grade=[]
print("Q72) :-")
for i in range(1,6):
    grade=int(input("     Enter Grade{}: ".format(i)))
    my_grade.append(grade)
    my_grade.sort()
den = len(my_grade)
result1=sum(my_grade[2:])
print("     Average grade: {0:.2f}".format(result1/(den-2)))

#Q74
starting_word = 'NAISNIENLGELTETWEORRSD'
crosses_out_word = ''
remaining_letters =''
for i in range(len(starting_word)):
    if(i%2==0):
        crosses_out_word=crosses_out_word+starting_word[i]
    else:
        remaining_letters=remaining_letters+starting_word[i]
print("Q74) Starting word: ",starting_word)
print("     Crossed out letters: ",' '.join(crosses_out_word))
print("     Remaining letters: ",' '.join(remaining_letters))

#Q76
print("Q76)  :-")
infile = open('states.txt','r')
states=[]
temp = []
for line in infile:
    line = line.rstrip()
    # line = line.lower()
    states.append(line)
infile.close
original=['Delaware','Pennsylvania','New Jersey','Georgia','Connecticut',
'Massachusetts','Maryland','South Carolina','New Hampshire','Virginia','New York','North Carolina','Rhode Island']
for i in range(50):
    if(states[i] in original):
        temp.append(states[i])
        temp.sort()
print('\n'.join(temp))

#Q78
special = int(input("Q78) Enter a four digit number: "))
mult = 4*special
temp = str(special)
rever = temp[::-1]
mult1 = str(mult)
if(rever==mult1):
    print("     {} is a special number".format(temp))
else:
    print("     {} is not a special number".format(temp))

#Q80
infile = open('USPres.txt','r')
for i,j in enumerate(infile,1):
    j = j.rstrip()
    if(i==34):
        print("Q80)",j)

#Q82
sum = 0
for i in range(1,1000001):
    while(i>0):
        temp=i%10
        sum=sum+temp
        i = i//10
print("Q82) The sum of the digits in the number from 1 to one million: {0:,}".format(sum))
