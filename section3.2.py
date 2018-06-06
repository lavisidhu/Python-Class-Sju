num = 4
if num<=9:
    print("{} {}".format("Q1)","Less than ten."))
elif num==4:
    print("{} {}".format("Q1)","Equal to four."))
print("{} {}".format("Q3)",('a'<'B'<'c')))
a=6
sentence=""
if ((3*a)-4)<12:
    sentence="Remember, "
print("{} {}".format("Q5)",(sentence+"tomorrow is another day.")))
a=2
b=3
c=5
if(a*b)<c:
    b=7
else:
    b=(c*a)
print("{} {}".format("Q7)",b))
letter = input("Q9) Enter A, B, or C: ")
letter = letter.upper() # change input to uppercase
if letter == "A":
    print("{} {}".format("   ","A, my name is Alice."))
elif letter == "B":
    print("{} {}".format("   ","To be, or not to be."))
elif letter == "C":
    print("{} {}".format("   ","Oh, say, can you see."))
else:
    print("{} {}".format("   ","You did not enter a valid letter."))
a=5
if(a>2) and ((a==3) or (a<7)):
    print("{} {}".format("Q11)","Hi"))
if "spam":
    print("{} {}".format("Q13)","A nonempty string is true.")) # nonempty list evaluates to true
else:
    print("{} {}".format("Q13)","A nonempty string is false")) # empty list evaluates to false
