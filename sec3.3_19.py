# #Q19
# born=1980
# year=born+1
# while True:
#     if (year-born)**2==year:
#         age=(year-born)
#         break
#     else:
#         year+=1
# print("Person will be {}\nin the year {}.".format(age,year))
#
# #Q21
# half_life=28
# weight=100
# final_weight=1
# time=1
# while True:
#     weight=weight/2
#     if weight<final_weight:
#         break
#     else:
#         time+=1
# print("The decay time is {} years.".format(time*half_life))
#
# #Q51
# decay_rate=12
# weight=10
# time=5
# for year in range(time):
#     weight=((100-12)/100)*weight
# print("The amount of cobalt-60 remaning\nafter {0:} years\
# is {1:.2f} grams.".format(time,weight))
#
# #Q53
# phrase=input("Enter a Phrase: ")
# phrase=phrase.lower().replace(" ","")
# vowel=['a','e','i','o','u']
# count=0
# for letter in phrase:
#     if letter in vowel:
#         count+=1
# print("The phrase contains {} vowels.".format(count))
#
# #Q55
# numerator=1
# denominator=1
# sum=0
# for denominator in range(1,101):
#     num=numerator/denominator
#     sum=sum+num
# print("The sum of 1+1/2+1/3+........+1/100\nis {0:.5f} to five\
# decimal places.".format(sum))
