def main():
    (initial_height,initial_velocity) = getinput()
    maximum_height = maxheight(initial_height,initial_velocity)
    time_drop = time(initial_height,initial_velocity)
    print("The maximum height of the ball is {0:.2f} feet.".format(maximum_height))
    print("The ball will hit the ground after approximately {0:.2f} seconds.".format(time_drop))

def getinput():
    while True:
        initial_height = eval(input("Enter the initial height of the ball: "))
        initial_velocity = eval(input("Enter the velocity of the ball: "))
        valid = isvalid(initial_height,initial_velocity)
        if valid is True:
            return (initial_height,initial_velocity)
            break
        else:
            continue

def isvalid(input1,input2):
    if input1>0 and input2>0:
        return True
    else:
        if input1<=0 and input2<=0:
            print("Entered intial height and intial velocity are invalid")
        elif input1<=0:
            print("Entered intial height is invalid")
        elif input2<=0:
            print("Entered velocity is invalid")

def maxheight(initial_height,initial_velocity):
    maximum_height = initial_height+(initial_velocity*(initial_velocity/32)-(16*((initial_velocity/32)**2)))
    return maximum_height

def time(initial_height,initial_velocity):
    height = 1
    time =0
    i=.01
    while height>0:
        height = initial_height+(initial_velocity*i)-(16*(i**2))
        time= time+.01
        i+=.01
    return time
main()
