def main():
    isbn = input("Enter an ISBN: ")
    isbn = isbn.replace("-", "")
    if isvalidisbn(isbn):
        print("The number is valid.")
    else:
        print("The number is not valid.")
def isvalidisbn(number):
    x = len(number)
    total = 0
    check = 10
    for i in range(0,x-1):
        if number[i].isdigit():
            total = total + (check*int(number[i]))
            check = check-1
        else:
            return False
    if number[-1].upper() == 'X':
        total=total+10
    elif number[-1].isdigit():
        total = total + (check*int(number[-1]))
    else:
        return False
    if total%11 == 0:
        return True

main()
