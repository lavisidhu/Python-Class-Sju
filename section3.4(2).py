#Q17
print("Q17)")
for i in range(1,5):
    print("Pass #" + str(i))
#Q19
print("Q19)")
num=5
for i in range(num,2*num-2):
    print(i)
#Q21
stringOfCents=""
for i in range(1, 11):
    stringOfCents +=chr(162) # chr(162) is cents sign
print("{} {}".format("Q21)",stringOfCents))
#Q23
print("Q23)")
for j in range(2,9,2):
    print(j)
print("Who do we appreciate?")
#Q25
number_of_sibilants = 0
word = "stargazers"
for ch in word:
    if(ch=='s') or (ch=='z'):
        number_of_sibilants+=1
print("{} {}".format("Q25",number_of_sibilants))
#Q27
word="183651"
sumOfOddIndexes=0
oddIndex=False # value set to false
for ch in word:
    if oddIndex:
        sumOfOddIndexes += int(ch) # for odd index value(notindex) is added
    oddIndex = not oddIndex
print("{} {}".format("Q27)",sumOfOddIndexes))
#Q29
for ch in "Python":
    continue
print("{} {}".format("Q29)",ch))
#31
numEvens=0
sumofEvens=0
list1=[2,9,6,7,12]
for num in list1:
    if num%2 == 0:
        numEvens += 1
        sumofEvens += num
print("{} {} {}".format("Q31)",numEvens,sumofEvens))
