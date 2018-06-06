verbalize = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion"]
def main():
    number = getNumber()
    temp = verbalizeNumber(number)
    verbalize_list = verbalize[:len(temp)]
    for i in range(1, len(temp)+1):
        print("{0:>5} {1}" .format(temp[-i], verbalize_list[-i]))

def getNumber():
    number = eval(input("Enter the positive whole number: "))
    isValid(number)
    return number

def isValid(number):
    if number < 0:
        print("Enter positive whole number.")
        getNumber()
    elif len(str(number)) > 27:
        print("Maximum allowed length is 27.")
        getNumber()

def verbalizeNumber(number):
    temp = []
    while number > 0:
        digit = number % 1000
        temp.append(digit)
        number = number // 1000
    return temp

main()
