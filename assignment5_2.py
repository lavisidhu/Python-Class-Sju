while True:
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    a=int(a)
    b=int(b)
    c=int(c)
    if(a!=0):
        test = (b**2)-(4*a*c)
        if(test>=0):
            solution1 = ((-1*b)+(test)**0.5)/(2*a)
            solution2 = ((-1*b)-(test)**0.5)/(2*a)
            print("solution: {0:.0f} and {1:.0f}".format(solution1,solution2))
        else:
            print("No solution")
        break
    else:
        print("Enter valid value of a")
        continue
