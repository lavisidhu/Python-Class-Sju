print("Q2)" + " " + 'c' + chr(35))
print("Q4)" + " " + chr(ord('B')))
list1 = [17, 3, 12, 9, 10]
list1.sort()
print("Q6)" + " " + "Minimum:",list1[0])
print("   " + " " + "Maximum:",list1[-1])
letter = 'D'
spread = ord('a') - ord('A')
print("Q8)" + " " + chr(ord(letter) + spread))
a = 2
b = 3
print("Q10)" + " " + str(((5-a)*b)<7))
print("Q12)" + " " + str(a ** b == b ** a))
print("Q14)" + " " + str(3e-2 < .01 * a))
print("Q16)" + " " + str((a * a < b) or not(a * a < a)))
print("Q18)" + " " + str(not(a < b) or not (a < (b + a))))
print("Q20)" + " " + str(((a == b) or not (b < a)) and ((a < b) or (b == a + 1))))
print("Q22)" + " " + str("Inspector" < "gadget"))
print("Q24)" + " " + str('J' >= 'J'))
print("Q26)" + " " + str('B' > '?'))
print("Q28)" + " " + str("Duck" < "Duck" + "Duck"))
print("Q30)" + " " + str("th" in "Python"))
print("Q32)" + " " + str((7 < 34) and ("7" < "34")))
print("Q34)" + " " + str(isinstance(32., int)))
print("Q36)" + " " + str(isinstance(32, int)))
print("Q38)" + " " + str("knight".startswith('n')))
print("Q40)" + " " + str("flute".endswith('t')))
print("Q42)" + " " + str(True and False))
print("Q44)" + " " + str(not False))
a = 2
b = 3
c = 4
d = 5
e = 6
x = not(a < b)
y = a > b
if x == y:
    print("Q46)" + " " + "Equivalent")
else:
    print("Q46)" + " " + "Not Equivalent")
x = not((a == b) or (a == c))
y = (a != b) and (a != c)
if x == y:
    print("Q48)" + " " + "Equivalent")
else:
    print("Q48)" + " " + "Not Equivalent")
x = (a < b) and ((a > d) or (a > e))
y = ((a < b) and (a > d)) or ((a < b) and (a > e))
if x == y:
    print("Q50)" + " " + "Equivalent")
else:
    print("Q50)" + " " + "Not Equivalent")
x = not(a >= b)
y = (a <= b) and not(a == b)
if x == y:
    print("Q52)" + " " + "Equivalent")
else:
    print("Q52)" + " " + "Not Equivalent")
str1 = "abc"
x = str1.upper() == str1
y = str1.isupper()
if x == y:
    print("Q54)" + " " + "Equivalent")
else:
    print("Q54)" + " " + "Not Equivalent")
print("Q56)" + " " + "(a!=b) and (a!=d)")
print("Q58)" + " " + "(a==b) or (a > b)")
print("Q60)" + " " + "(a == "") or (a > b) or (len(a) > 5)")
print("Q62)" + " " + "name in ('Athos','Porthos','Aramis')")
print("Q64)" + " " + "2010<=year<=2013")
print("Q66)" + " " + "1<n<=22")
print("Q68)" + " " + "100<=n<=200")
print("Q70)" + " " + str("colonel".startswith('k')))
str1 = "target"
str2 = "get"
print("Q72)" + " " + str(str1.endswith(str2)))
str1 = "Teapot"
print("Q74)" + " " + str(str1.startswith(str1[0:4])))
str1 = "spam and eggs"
print("Q76)" + " " + str(str1.endswith(str1[10:len(str1)])))
num = "1234.56"
print("Q78)" + " " + str(isinstance(num, float)))
print("Q80)" + " " + str(isinstance("25", int)))
letter = ord('M')
print("Q82)" + " " + str(isinstance(letter, str)))
print("Q84)" + " " + str("seven".isdigit()))
