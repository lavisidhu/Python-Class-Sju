
infile=open("Units.txt","r")
length=[]
temp=[]
lendict={}

for line in infile:
    line=line.rstrip()
    length.append(line)

for element in length:
    temp=element.split(',')
    lendict[temp[0]]=float(temp[1])
print("UNITS OF LENGTH")
units=list(lendict.keys())
for i in range(int(len(lendict)/3)):
    print("{0:<10s}{1:<10s}{2:<10s}".format(units[i],units[i+1],units[i+2]))
convert_from=input("\nUnits to convert from: ")
convert_to=input("Units to convert to: ")
initial=eval(input("Enter length in {}: ".format(convert_from)))

old=lendict.get(convert_from,0)
new=lendict.get(convert_to,0)
old_feet=initial*old
if old==0 or new==0:
    print("Invalid input")
else:
    print("Length in {}: {}".format(convert_to,round(old_feet/new,3)))
