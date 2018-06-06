states=["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina","Rhode Island","Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri","Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin","California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska","Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]
print("Q1)" + " " + states[1], states[-1])
print("Q3)" + " " + states[48], states[49])
print("Q5)" + " " + str(states.index("Alaska")))
print("Q7)" + " " + states[states.index("Ohio")])
print("Q9)" + " " + states[len(states) - 1], states[-1])
states[0] = states[0].upper()
print("Q11)" + " " + states[0])
states.append(["Puerto Rico"]) # append() add element at end of the list
print("Q13)" + " " + str(states[50]))
states.insert(0, "United States") # insert at defined location
print("Q15)" + " " + states[0])
print("Q17)" + " " + str(states[2:5])) # according to new list with "United States"
print("Q19)" + " " + str(states[-5:-2])) # according to new list with "Puerto Rico"
print("Q21)" + " " + str(states[:4]))
print("Q23)" + " " + str(states[-3:]))
print("Q25)" + " " + str(states[3:3])) # return empty list ( from 3 to (3-1) move left to right)
print("Q27)" + " " + str(states[1:10][2])) # double slicing, first sublist is formed then return 2nd index value from sublist
print("Q29)" + " " + str(states[-2:len(states)])) # return value from index -2 to index(51-1) * + - taken at a time
