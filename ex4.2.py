#Q49
def main():
    weight = eval(input("Enter the number of ounces: "))
    price = cost(weight)
    print("Cost: ${0:.2f}".format(price))
def cost(ounces):

    if ounces >= 1:
        cost = .05 + (.10*ceil(ounces-1))
        return cost
    else:
        return 0
def ceil(i):
    if i == int(i):
        return i
    else:
        i = int(i+1)
        return i
main()

#Q51
def main():
    word1 = input("Enter the first word or phrase: ")
    word2 = input("Enter the second word or phrase: ")
    if areAnagrams(word1,word2):
        print("Are anagrams")
    else:
        print("Are not anagrams")

def areAnagrams(string1,string2):
    string1 = sorted(ch for ch in string1.lower() if ch.isalnum())
    string2 = sorted(ch for ch in string2.lower() if ch.isalnum())
    return(string1==string2)
main()

#Q53
def main():
    pres = [("Lyndon", "Johnson"),("John", "Kennedy"),("Andrew", "Johnson")]
    pres.sort(key=lambda president: president[1])
    pres.sort(key=lambda president: president[0])
    for president in pres:
        print("{},{}".format(president[1],president[0]))
main()

#Q55
def main():
    NE = [("Maine", 30840, 1.329), ("Vermont", 9217, .626), ("New Hampshire", 8953,
    1.321), ("Massachusetts", 7800, 6.646), ("Connecticut", 4842, 3.59), ("Rhode Island", 1044, 1.05)]
    NE.sort(key=lambda state: state[1], reverse=True)
    for state in NE:
        print(state[0],end="  ")
main()

#Q57
def main():
    NE = [("Maine", 30840, 1.329), ("Vermont", 9217, .626), ("New Hampshire", 8953,
    1.321), ("Massachusetts", 7800, 6.646), ("Connecticut", 4842, 3.59), ("Rhode Island", 1044, 1.05)]
    NE.sort(key=lambda state: state[2]/state[1])
    for state in NE:
        print(state[0],end="  ")
main()

#Q59
def main():
    numbers = eval(input("Enter the numbers(comma separated): "))
    numbers = list(numbers)
    # numbers=[865,1169,1208,1243,290]
    numbers.sort(key=max_prime_factor)
    print("Sorted by largest prime factor:")
    print(numbers)
def max_prime_factor(number):
    max=1
    for i in range(2,number):
        if(number%i==0):
            prime=1
            for j in range(2,i):
                if(i%j==0):
                    prime=0
            if(prime==1):
                if i > max:
                    max = i
    return max
main()

#Q61
def main():
    numbers=[865,1169,1208,1243,290]
    numbers.sort(key=sum_of_odddigits, reverse = True)
    print("Sorted by sum of odd digits:")
    print(numbers)
def sum_of_odddigits(number):
    sum = 0
    digit_string = str(number)
    for digit in digit_string:
        digit = int(digit)
        if digit%2!=0:
            sum = sum+digit
    return sum
main()

#Q63
def main():
    infile = open("USPres.txt","r")
    presidents=[]
    for line in infile:
        line = line.rstrip()
        line = line.split(" ")
        presidents.append(line)
    presidents.sort(key=sort_pres_len_firstname)
    for pres in presidents[0:6]:
        pres = " ".join(pres)
        print(pres)

def sort_pres_len_firstname(name):
    length = len(name[0])
    return length

main()

#Q65
def main():
    infile = open("States.txt","r")
    states =[]
    for line in infile:
        line = line.rstrip()
        states.append(line)
    states.sort(key=sort_no_of_vowels, reverse=True)
    for state in states[0:6]:
        print(state)

def sort_no_of_vowels(string):
    vowel = ['a','e','i','o','u']
    string = string.lower()
    count = 0
    for ch in string:
        if ch in vowel:
            count = count+1
    return count

main()

#Q67
def main():
    credit_input()
    credit_calculation(old_balance,charges,credit)
    credit_output(new_balance,minimum_payment)

def credit_input():
    global old_balance
    global charges
    global credit
    old_balance = eval(input("Enter Old Balance: "))
    charges = eval(input("Enter charges for month: "))
    credit = eval(input("Enter Credits: "))
    return old_balance,charges,credit

def credit_calculation(old_balance,charges,credit):
    global new_balance
    global minimum_payment
    interst = .015*old_balance
    new_balance = old_balance+interst+charges-credit
    if new_balance<=20:
        minimum_payment = new_balance
    else:
        minimum_payment = 20 + (.1*(new_balance-20))
    return new_balance,minimum_payment

def credit_output(new_balance,minimum_payment):
    print("New Balance: ${0:.2f}".format(new_balance))
    print("Minimum Payment: ${0:.2f}".format(minimum_payment))

main()

#Q69
def main():
    earnings_input()
    earnings_calculation(hours_worked,hourly_pay)
    earnings_output(week_pay)

def earnings_input():
    global hours_worked
    global hourly_pay
    hours_worked = eval(input("Enter hours worked: "))
    hourly_pay = eval(input("Enter hourly pay: "))
    return hours_worked,hourly_pay

def earnings_calculation(hours_worked,hourly_pay):
    global week_pay
    if hours_worked > 40:
        week_pay = (hourly_pay*40)+((1.5*hourly_pay)*(hours_worked-40))
        return week_pay
    else:
        week_pay = (hourly_pay*hours_worked)
        return week_pay

def earnings_output(week_pay):
    print("Week's pay: ${0:.2f}".format(week_pay))

main()
