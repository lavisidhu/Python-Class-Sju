def main():
    infile=txt_list("Exchrate.txt")
    country_list=[]
    temp=[]
    exch_dict={}
    for country in infile:
        country=country.split(',')
        country[2]=float(country[2])
        country_list.append(country)
    country_list.sort(key=lambda x: x[2])

    for element in infile:
        temp=element.split(',')
        temp[2]=float(temp[2])
        exch_dict[temp[0]]=(temp[1],temp[2])

    while True:
        entry=user_input()
        out_display(entry,exch_dict,country_list)


def user_input():
    print("1. Currency and exchange rate info.\n2. List of countries in order \
of dollar purchasing power.\n3. Currency conversion.\n4. Quit")
    entry=input("ENTER YOUR CHOICE: ")
    return entry

def txt_list(filename):
    infile=open(filename,"r")
    list_of_text=[]
    for line in infile:
        line=line.rstrip()
        list_of_text.append(line)
    return list_of_text

def out_display(entry,exch_dict,country_list):
    if entry=='1':
        country=input("Enter the name of a country: ")
        currency=exch_dict.get(country.title(),('none','none'))
        print("Currency:",currency[0])
        print("Exchange rate:",currency[1])
        quit()

    if entry=='2':
        for country in country_list:
            print(country[0])
        quit()

    if entry=='3':
        first_country=input("Enter name of first country: ")
        second_country=input("Enter name of second country: ")
        amount=float(input("Amount of money to convert: "))
        first=exch_dict.get(first_country.title(),(0,1))
        second=exch_dict.get(second_country.title(),(0,0))
        if first[1] and second[1] != 0:
            exchange_price=(1/first[1])*second[1]*amount
            print("{} {}s from {} equals {} {}s from {}.".format(amount,
            first[0],first_country.title(),exchange_price,
            second[0],second_country.title()))
            quit()

    if entry=='4':
        print("**************Thank You***************")
        quit()

    else:
        print("Invalid Entry")

main()
