# #Q8
# infile=open("DOW.txt","r")
# line_list=[]
# for line in infile:
#     line_list.append(line.split(","))
# for list in line_list:
#     performance=(eval(list[5])-eval(list[4]))/eval(list[4])
#     list.append(performance)
# line_list.sort(key=lambda x: x[-1] , reverse=True)
# print("Best performing stock: {0:} {1:.2%}".format(line_list[0][0],
#         line_list[0][-1]))
# print("Worst performing stock: {0:} {1:.2%}".format(line_list[-1][0],
#         line_list[-1][-1]))


# #Q10
# infile=open("DOW.txt","r")
# line_list=[]
# for line in infile:
#     line_list.append(line.split(","))
# line_list.sort(key=lambda x: eval(x[5]))
# print("{0:<20s}{1:20s}{2:>10s}".format("Company","Symbol",
# "Price on 12/31/2013"))
# for i in range(5):
#     print("{0:<20s}{1:20s}${2:s}".format(line_list[i][0],line_list[i][1],
#     line_list[i][5]))

# #Q12
# infile=open("Justices.txt","r")
# current_justice=[]
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     # print(line)
#     if line[5]=='0':
#         current_justice.append(line)
# current_justice.sort(key=lambda x:eval(x[4]))
# print("Current Justices:")
# for name in current_justice:
#     print("{} {}".format(name[0],name[1]))

# #q14
# infile=open("Justices.txt","r")
# state=input("Enter a State abbreviation: ")
# current_justice=[]
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     if line[3].upper()==state.upper():
#         current_justice.append(line)
# if current_justice!=[]:
#     current_justice.sort(key=lambda x:eval(x[5])-eval(x[4]), reverse=True)
#     print("{0:<20s}{1:20s}{2:>10s}".format("Justice","Appointing Pres","Yrs Served"))
#     for name in current_justice:
#         if name[5]!="0":
#             years_served=eval(name[5])-eval(name[4])
#
#         else:
#             years_served="2015-{}".format(name[4])
#
#         name[2]=name[2].split()
#         print("{0:<s} {1:<14s}{2:<20s}{3:<20}".format(name[0],name[1],name[2][-1],years_served))
# else:
#     print("No Justice from this state.")

# #16
# infile=open("Pioneers.txt","r")
# comp_list=[]
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     comp_list.append(line)
# length=int(int(len(comp_list))/4)
# for i in range(length):
#     print("{0:<20s}{1:<20s}{2:<20s}{3:<20s}".format(comp_list[i][0],
#     comp_list[i+1][0],comp_list[i+2][0],comp_list[i+3][0]))
#     i=i+4
# name = input("\nEnter the name of a computer pioneer: ")
# name=name.title()
# for pioneer in comp_list:
#     if pioneer[0]==name:
#         spec=pioneer[1]
#         break
#     else:
#         spec="is Wrong Input"
# print("{}  {}".format(name,spec))

# #Q18)
# infile=open("Colleges.txt","r")
# state=input("Enter a state abbreviation: ")
# college=[]
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     if line[1]==state.upper():
#         college.append(line)
# college.sort(key=lambda x: eval(x[2]))
# if college!=[]:
#     print("Last college in {} founded before 1800:\n{}".format(state.upper(),
#     college[-1][0]))
# else:
#     print("No college in state.")

# #Q20
# infile=open("StatesANC.txt","r")
# state=input("Enter the name of a state: ")
# flag='n'
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     if line[0].upper()==state.upper():
#         print("Abbreviation: {}\nNickname: {}\nCapital: {}".format(line[1],
#         line[2],line[3]))
#         flag='y'
#         break
# if flag=='n':
#     print("State not found or wrong input")

# #Q22
# infile=open("Oscars.txt","r")
# year_user=input("Enter year from 1928-2013: ")
# year=1928
# flag='n'
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     line.append(year)
#     year=year+1
#     if line[2]==int(year_user):
#         print("Best Film: ",line[0])
#         print("Genre: ",line[1])
#         flag='y'
#         break
# if flag=='n':
#     print("Wrong Input")

# #Q24)
# infile=open("Cowboy.txt","r")
# outfile=open("Cowboy2.txt","w")
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     line[1]=0.80*eval(line[1])
#     line[1]=str(line[1])
#     line=",".join(line)
#     outfile.write(line+'\n')
# infile.close()
# outfile.close()

# #Q26)
# outfile=open("Cowboy.txt","a")
# line=["Winchester Rifle","20.50"]
# line=",".join(line)
# outfile.writelines(line+'\n')
