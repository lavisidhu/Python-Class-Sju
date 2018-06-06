# #Q45
# pres_name = input("Who was the youngest U.S. president? ")
# pres_name = pres_name.upper()
# output1="Correct. He became president at age 42\n" + \
# "when President McKinley was assassinated."
# output2="Incorrect. He became president at age 43. However,\n" + \
# "he was the youngest person elected president."
# output={"THEODORE ROOSEVELT":output1,"TEDDY ROOSEVELT":output1,
# "JFK":output2,"JOHN KENNEDY":output2,"JOHN F. KENNEDY":output2}
# print(output.get(pres_name,"Nope"))

# #Q47)
# tophitters = {"Gehrig":{"atBats":8061, "hits":2721},
#             "Ruth":{"atBats":8399, "hits":2873},
#             "Williams":{"atBats":7706, "hits":2654}}
# for player in tophitters:
#     print("{0:<10}{1:.3f}".format(player,
#     (tophitters[player]["hits"]/tophitters[player]["atBats"])))

# #Q49
# tophitters = {"Gehrig":{"atBats":8061, "hits":2721},
#             "Ruth":{"atBats":8399, "hits":2873},
#             "Williams":{"atBats":7706, "hits":2654}}
# hits=0
# count=0
# for player in tophitters:
#     hits=hits+tophitters[player]["hits"]
#     count=count+1
# print("The average number of hits by\nthe baseball players was \
# {0:.2f}".format(hits/3))

# #Q51)
# import pickle
# infile = open("JusticesDict.dat", 'rb')
# justicedict = pickle.load(infile)
# infile.close()
# flag='n'
# pres_name = input("Enter a president: ")
# for x in justicedict:
#     if justicedict[x]["pres"].title() == pres_name.title():
#         print(" {0:16} {1:d}".format(x, justicedict[x]["yrAppt"]))
#         flag='y'
# if flag=='n':
#     print("Invalid Entry")

# #Q53)
# import pickle
# infile = open("JusticesDict.dat", 'rb')
# justicedict = pickle.load(infile)
# infile.close()
# flag='n'
# justice_name = input("Enter name of a justice: ")
# for x in justicedict:
#     if x.title() == justice_name.title():
#         print("Appointed by: {}".format(justicedict[x]["pres"]))
#         print("Sate: {}".format(justicedict[x]["state"]))
#         print("Year of appointment: {}".format(justicedict[x]["yrAppt"]))
#         if justicedict[x]["yrLeft"]==0:
#             print("Currently serving on Supreme Court")
#         else:
#             print("Served: {} - {}".format(justicedict[x]["yrAppt"],
#             justicedict[x]["yrLeft"]))
#         flag='y'
# if flag=='n':
#     print("Invalid Entry")

# #Q55)
# sentence=input("Enter a sentence")
# sentence=sentence.upper()
# sentence=sentence.replace(""," ")
# sentence=sentence.split()
# sentence.sort()
# letterdict=dict((sentence[n],0 )for n in range(len(sentence)))
# for letter in sentence:
#     letterdict[letter]+=1
# letterdict=sorted(letterdict.items(), key=lambda x: x[1],reverse=True)
# letterdict=dict(letterdict)
# for letter in letterdict:
#     print("{}: {}".format(letter,letterdict[letter]))

# #Q57)
# import pickle
#
# infile=open("USpresStatesDict.dat","rb")
# presdict=pickle.load(infile)
# infile.close()
#
# statedict={}
#
# for state in presdict.values():
#     if statedict.get(state, False):
#         statedict[state] += 1
#     else:
#         statedict[state] = 1
#
# state_sorted=[state for state in statedict if statedict[state]>2]
# state_sorted.sort(key=lambda x: statedict[x],reverse=True)
# print("States that produced three or\nmore presidents as of 2016:\n")
# for state in state_sorted:
#     print("{}: {}".format(state,statedict[state]))

# #Q61
# import pickle
# infile=open("LargeCitiesDict.dat","rb")
# citydict=pickle.load(infile)
# infile.close()
# no_of_city={}
# for state in citydict:
#     no_of_city[state]=len(citydict[state])
# user_input=int(input("Enter an integer from 0 to 13: "))
# print("The following states have exactly {} large cities.".format(user_input))
# for state in no_of_city:
#     if no_of_city[state]==user_input:
#         print(state,end="  ")
# print("\n")

# #Q59
# infile=open("calender.csv","r")
# mylist=[]
# day=""
# for line in infile:
#     line=line.rstrip()
#     line=line.split(",")
#     mylist.append(line)
# infile.close()
# calender_dict=dict(mylist)
# date_user=input("Enter a date in 2015(m/d/yy): ")
# for date in calender_dict:
#     if date==date_user:
#         day=calender_dict[date]
# print("{} falls on a {}".format(date_user,day))
