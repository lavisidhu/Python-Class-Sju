a=int(2)
b=int(3)
"""
print("Q9)" + " " + str(3*a == 2*b))
print("Q11)" + " " + str(b<=3))
print("Q13)" + " " + str((a**(5-2))>7))
print("Q15)" + " " + str((a<b) or (b<a)))
print("Q17)" + " " + str(not((a<b) and(a < (b+a)))))
print("Q19)" + " " + str(((a==b) and (a*a<b*b)) or ((b<a) and (2*a<b))))
"""
print("{} {}".format("Q9)",(3*a==2*b))) # == compare and return result in T or F
print("{} {}".format("Q11)",(b<=3)))
print("{} {}".format("Q13)",(a**5-2>7)))
print("{} {}".format("Q15)",((a<b) or (b<a)))) # or function(if one is true, return true)
print("{} {}".format("Q17)",(not((a<b) and (a<(b+a)))))) # not reverse the value, and function(all need to be true to return true)
print("{} {}".format("Q19)",((a==b) and (a*a<b*b) or ((b<a) and (2*a<b)))))
