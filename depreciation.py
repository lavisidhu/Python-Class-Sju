def main():
    item, year, cost, life, method = get_input()
    method = method.upper()
    if (method == 'SL'):
        print("Description: ",item)
        print("Year of purchase: ",year)
        print("cost: ${0:,.2f}".format(cost))
        print("Estimated life: {} years ".format(life))
        print("Method of depriciation: Sraight - line")
        print("{0:10}{1:20}{2:10}{3:10}".format("year","Beg Balance","Deprec","Total Depreciation"))
        SL(cost,life,year)
    else:
        print("Description: ",item)
        print("Year of purchase: ",year)
        print("cost: ${0:,.2f}".format(cost))
        print("Estimated life: {} years ".format(life))
        print("Method of depriciation: double-declining balance")
        print("{0:10}{1:20}{2:10}{3:10}".format("year","Beg Balance","Deprec","Total Depreciation"))
        DDB(cost,life,year)

def get_input():
    item = input("Enter name of item purchased: ")
    year = eval(input("Enter year purchased: "))
    cost = eval(input("Enter cost of item: "))
    life = eval(input("Enter estimated life of item (in years): "))
    method = input("Enter method of depreciation (SL or DDB): ")
    return item, year, cost, life, method

def DDB(cost,life,year):
    total_dep = 0
    for i in range(life):
        dep = (2/life)*cost
        if(i == (life-1)):
            dep = cost
        total_dep = total_dep + dep
        print("{0:}{1:15,.2f}{2:20,.2f}{3:20,.2f}".format(year,cost,dep,total_dep))
        cost = cost-dep
        year+=1

def SL(cost,life,year):
    begn_balance = cost
    total_dep = 0
    for j in range(life):
        dep = (1/life)*cost
        total_dep = total_dep + dep
        print("{0:}{1:15,.2f}{2:20,.2f}{3:20,.2f}".format(year,begn_balance,dep,total_dep))
        begn_balance = begn_balance - dep
        year+=1
main()
