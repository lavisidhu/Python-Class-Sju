def main():
    number = get_input()
    (max_factor,min_factor)  = prime_factor(number)
    print("Largest prime factor: ",max_factor)
    print("Smallest prime factor: ",min_factor)
def get_input():
    number = eval(input("Enter a positive integer > 1: "))
    return (number)
def prime_factor(number):
    max_factor = 1
    min_factor = number
    for i in range(2,number):
        if(number%i==0):
            prime=1
            for j in range(2,i):
                if(i%j==0):
                    prime=0
            if(prime==1):
                if i > max_factor:
                    max_factor = i
                if i < min_factor:
                    min_factor = i

    return (max_factor,min_factor)
main()
