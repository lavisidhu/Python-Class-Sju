#Q25
def maximum(list):
    length = len(list)
    check=0
    for i in range(length):
        for j in range(length):
            if list[i]>=list[j]:
                check=1
            else:
                check=0
                break
        if check==1:
            return list[i]
            break
list_test = [2,3,1,4,2,7,12,9,5]
print(maximum(list_test))

#Q27
def main():
    word = input("Enter a Word: ")
    qwerty(word)
def qwerty(string):
    check_qwerty = ['q','w','e','r','t','y','u','i','o','p']
    string = string.lower()
    result =""
    for letter in string:
        if letter in check_qwerty:
            result = "true"
        else:
            result = "false"
            break
    if result=="true":
        print("{} is a QWERTY word".format(string.upper()))
    else:
        print("{} is not a QWERTY word".format(string.upper()))
main()

# Q29
def main():
    pay_1 = option1()
    pay_2 = option2()
    print("option1 pays ${0:.2f}\noption2 pays ${1:.2f}".format(pay_1,pay_2))
    if pay_1>pay_2:
        print("Option1 is better.")
    elif pay_1==pay_2:
        print("Both Options are same.")
    else:
        print("Option2 is better.")
def option1():
    final_pay_1 = 10*100
    return final_pay_1
def option2():
    final_pay_2 = 1
    increment = 1
    for day in range(1,10):
        increment = 2*increment
        final_pay_2 = final_pay_2 + increment
    return final_pay_2
main()

#Q31
def main():
    curearnings,ytdearnings,totalearnings = wage_base()
    ssn_tax = social_security_tax_rate(curearnings,ytdearnings,totalearnings)
    medicare_tax = medicare_rate(curearnings,ytdearnings,totalearnings)
    ficatax = ssn_tax + medicare_tax
    print("FICA tax for the current pay period: ${0:0,.2f}".format(ficatax))

def wage_base():
    ytdearnings = eval(input("Enter total earnings for this year prior to current pay period: "))
    curearnings = eval(input("Enter total earnings for the current pay period: "))
    totalearnings = ytdearnings+curearnings
    return (curearnings,ytdearnings,totalearnings)

def social_security_tax_rate(curEarnings,ytdEarnings,totalEarnings):
    socialSecurityBenTax = 0
    if totalEarnings <= 117000:
        socialSecurityBenTax = 0.062 * curEarnings
    elif ytdEarnings < 117000:
        socialSecurityBenTax = 0.062 * (117000 - ytdEarnings)
    return socialSecurityBenTax

def medicare_rate(curEarnings,ytdEarnings,totalEarnings):
    medicareTax = 0.0145 * curEarnings
    if ytdEarnings >= 200000:
        medicareTax += 0.009 * curEarnings
    elif totalEarnings > 200000:
        medicareTax += 0.009 * (totalEarnings - 200000)
    return medicareTax

main()

#Q33
colors = []
def main():
    letter = request()
    list_colors(letter)
    display()
def request():
    word = input("Enter a letter: ")
    word = word.upper()
    return word
def list_colors(word):
    global colors
    infile = open("Colors.txt","r")
    for line in infile:
        line = line.rstrip()
        if line.startswith(word):
            colors.append(line)
    infile.close()


def display():
    for color in colors:
        print("  ",color)
main()
