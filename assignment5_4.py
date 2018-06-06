card = input("Enter credit card number: ")
x = len(card)
if(x==14):
    sum1 = 0
    sum2 = 0
    for i in range(14):
        if(i%2==0):
            temp=(2*int(card[i]))
            if(len(str(temp))>=2):
                temp = int(temp)
                temp=temp-9
            temp=int(temp)
            sum1=sum1+temp
        else:
            sum2=sum2+int(card[i])
    total = sum1+sum2
    if(total%10==0):
        print("The number is valid")
    else:
        print("The number is not valid")
else:
    print("Enter number is not valid")
