def main():
    result = isTripleConsecutive()
    if result == True:
        print("{} contains three successive letters\nin consecutive order.".format(word))
    else:
        print("{} does not contains three successive letters\nin consecutive order.".format(word))

def isTripleConsecutive():
    global word
    word = input("Enter a word: ")
    word = word.upper()
    x = len(word)
    count = 0
    for i in range(x-1):
        if ord(word[i+1])- ord(word[i]) == 1:
            count=count+1
        else:
            if count >= 2:
                break
            else:
                count = 0
    if count >= 2:
        return True
    else:
        return False
main()
