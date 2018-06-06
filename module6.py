#Q17
def main():

    number1,number2=get_input()
    divisor_number1=divisors(number1)
    divisor_number2=divisors(number2)
    common_list=common_divisor(divisor_number1,divisor_number2)
    print("Greatest common divisor:",max(common_list))


def get_input():
    while True:
        try:
            value1=int(input("Enter the first non zero number: "))
            value2=int(input("Enter the second non zero number: "))
            if (value1<=0 or value2<=0):
                print("Enter correct values.")
            else:
                return int(value1),int(value2)
                break
        except:
            print("Enter correct values.")

def divisors(number):
    divisors_list=[]
    for divisor in range(1,number+1):
        if number%divisor==0:
            divisors_list.append(divisor)
    return divisors_list

def common_divisor(list1,list2):
    common_list=[]
    for item in list1:
        if item in list2:
            common_list.append(item)
    return common_list

main()
