#Q16
restitut = eval(input("Q16) Enter coefficient of restitution: "))
int_height = eval(input("     Enter initial height in meters: "))
count = 1
temp_dist = int_height
rise = restitut*int_height
temp_height = 0
while(rise>=.10):
    count = count+1
    temp_dist =(restitut*temp_dist)
    temp_height = temp_height+temp_dist
    rise = restitut*rise
dist= int_height + (2*temp_height)
print("{0} Number of bounces: {1} ".format((4*" "),count))
print("{0} Meters traveled: {1:.2f} ".format((4*" "),dist))

#18
post_int =eval(input("Q18) Enter a positive integer(>1): "))
prime_fact=[]
for i in range(2,post_int):
    if(post_int%i==0):
        prime=1
        for j in range(2,i):
            if(i%j==0):
                prime=0
        if(prime==1):
            prime_fact.append(i)
print("{0} Prime factors are: {1}".format((4*" "),str(prime_fact).strip('[]')))

#Q20
population = 7
growth_rate = .011
year = 2011
count=0
new_population = population
while(new_population<=8):
    count=count+1
    new_population=1.011*new_population
print("Q20) World population will be 8 billion in the year",year + count)

#Q22
#cpi_1913 = 9.9
#cpi_183 = 100
cpi_2014 = 238.25
growth = .025
exp_cpi=cpi_2014
count=0
while(exp_cpi<=(2*cpi_2014)):
    count=count+1
    exp_cpi=1.025*exp_cpi
print("Q22) Consumer price will double in {0:} years".format(count))

#Q24
deposit = 100
interst = .03
balance = 0
count = 0
while(balance<=3000):
    balance=balance+((interst/12)*balance)+deposit
    count=count+1
print("Q24) Annuity will be worth more than $3000 after {} months.".format(count))

#Q26
dec_rate=.00012
weight = 1
count = 0
while(.50<weight<=1):
    weight = (1-dec_rate)*weight
    count = count+1
print("Q26) Carbon-14 has a half life of {} years.".format(count))

#28
deposit = eval(input("Q28) Enter amount of deposit: "))
interst = .036
balance = deposit
count = 0
while(balance>=600):
    balance=balance+((interst/12)*balance)-600
    count=count+1
print("    Balance will be ${0:.2f} after {1:} months.".format(balance,count))

#30
coffee_temp = 212
room_temp = 70
k = .079
count = 0
while(coffee_temp>=150):
    count = count+1
    coffee_temp = coffee_temp - (k*(coffee_temp-room_temp))
print("Q30) The coffee will cool to below 150 degrees in {} minutes.".format(count))
