print("{} {}".format("Q2)",list(range(-11,-7)))) ##print(*range(-11,-7))
print("{} {}".format("Q4)",list(range(2010,2030,5))))
print("{} {}".format("Q6)",list(range(1))))
print("{} {}".format("Q8)",list(range(12,2,-5))))
for i in range(3, 7):
    print("{} {}".format("Q18)",2 * i))
for i in range(-9, 0, 3):
    print("{} {}".format("Q20)",i))
n = 3
total = 0
for i in range(1, n + 1):
    total += i
print("{} {}".format("Q22)",total))
for countdown in range(10, 0, -1):
    print("{} {}".format("Q24)",countdown))
numCaps = 0
name = "United States of America"
for ch in name:
    if ch.isupper():
        numCaps += 1
print("{} {}".format("Q26)",numCaps))
word = "cloudier"
newWord = ""
evenIndex = True
for ch in word:
    if evenIndex:
        newWord += ch
    evenIndex = not evenIndex
print("{} {}".format("Q28)",newWord))
for ch in "Python":
    break
print("{} {}".format("Q30)", ch))
list1 = [2,9,6,7,13,3]
maxOfOdds = 0
for num in list1:
    if (num % 2 == 1) and (num > maxOfOdds):
        maxOfOdds = num
print("{} {}".format("Q32)",maxOfOdds))
numOfNumbers = 0
list1 = ["three", 4, 5.7, "six", "seven", 8, 3.1416]
for item in list1:
    if isinstance(item, str):
        continue
    numOfNumbers += 1
print("{} {}".format("Q34)",numOfNumbers))
# #I'm looking over a four leaf clover.
leaves = ("sunshine","rain", "the roses that bloom in the lane", "somebody I adore")
number = 1
for leaf in leaves:
    print("{} {} {} {}".format("Q36)","Leaf", str(number) + ':', leaf))
    number += 1
dataList = []
infile = open("Numbers.txt", 'r')
for line in infile:
    dataList.append(eval(line))
infile.close()
print("Q38)" + " " + str(sum(dataList)))
infile = open("States.txt", 'r')
for line in infile:
    continue
infile.close()
print("Q40)" + " " + line, end="")
