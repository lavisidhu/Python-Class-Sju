firstname=[]
lastname=[]
beginingbalance=[]
newbalance=[]
operation=[]
accountnumbers = []
def main():
    i=0
    while True:
        print("Bank account application\n\t1) Create new account\n\t2) Credit/Debit an\
 account\n\t3) List all accounts\n\t4) List account history\n\t5) Quit")
        choice = input("What would you like to do: ")

        if choice == '1':
            create(firstname,lastname,beginingbalance,newbalance,i)
            i=i+1

        elif choice =='2':
            credit_debit(operation,beginingbalance,newbalance)

        elif choice =='3':
            listaccount()

        elif choice =='4':
            transaction()

        elif choice =='5':
            print("*****Thank you*******")
            break

        else:
            print("Enter valid option")


def create(firstname,lastname,beginingbalance,newbalance,i):
    temp=[]
    temp1=[]
    print("Creating a new account.....")
    print("Please enter the individuals")
    firstname.append(input("\tFirst Name: "))
    lastname.append(input("\tLast Name: "))
    beginingbalance.append(float(input("\tBeginning Balance (USD): ")))
    temp.append(beginingbalance[i])
    newbalance.append(temp)
    operation.append(temp1)
    accountnumbers.append(i+1)
    print("New account created for {} {} {} {}{}".format(firstname[i].title(),lastname[i].title(),'(Account#',i+1,')'))
    i=i+1


def credit_debit(operation,beginingbalance,newbalance):
    global account,amount
    print("Crediting/Debiting account.....")
    account=int(input("Please enter the account number: "))
    amount=float(input("Please enter the amount: "))
    valid = isvalid(account)
    if valid is True:

        if amount < 0:
            operation[account-1].append('-$'+str(abs(amount)))
            beginingbalance[account-1]=float(beginingbalance[account-1])+float(amount)
            newbalance[account-1].append(beginingbalance[account-1])
            print("{0:} {1:} (Account# {2:}) debited ${3:.2f}".format(firstname[account-1].title(),lastname[account-1].title(),account,abs(amount)))
            print("New balance: ${} ".format(beginingbalance[account-1]))
        else:
            operation[account-1].append('+$'+str(abs(amount)))
            beginingbalance[account-1]=float(beginingbalance[account-1])+float(amount)
            newbalance[account-1].append(beginingbalance[account-1])
            print("{0:} {1:} (Account# {2:}) credited ${3:.2f}".format(firstname[account-1].title(),lastname[account-1].title(),account,amount))
            print("New balance: ${}".format(beginingbalance[account-1]))


def listaccount():
    print("Listing accounts....")
    for i in range(len(firstname)):
        print("{}\t{} {}\t${}".format(i+1,firstname[i].title(),lastname[i].title(),beginingbalance[i]))


def transaction():
    print("Transaction history")
    account = int(input("Enter the account number: "))
    valid = isvalid(account)
    if valid is True:
        print("{}\t{} {}".format(account,firstname[account-1].title(),lastname[account-1].title()))
        for j in range(len(operation[account-1])):
            print("${}\t\t\t{}".format(newbalance[account-1][j],operation[account-1][j]))
        print("${}".format(beginingbalance[account-1]))


def isvalid(account):
    if account in accountnumbers:
        return True
    else:
        print("Enter valid account number")


main()
