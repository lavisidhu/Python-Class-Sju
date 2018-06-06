# #Q26
# def main():
#     string="Geeks for geeks."
#     substring="gee"
#     count=my_count(string,substring)
#     print(count)
#
# def my_count(string,substring):
#     string=string.lower().replace(" ","")
#     substring=substring.lower().replace(" ","")
#     check=len(substring)-1
#     count=0
#     while True:
#         if substring in string:
#             index=string.find(substring)
#             string=string[index+check:]
#             count=count+1
#         else:
#             break
#     return count
# 
# main()
#
#
# #Q28
# def main():
#     number=getN()
#     factorial=fact(number)
#     print("{}! is {}.".format(number,factorial))
#
# def getN():
#     while True:
#         try:
#             number=int(input("Enter a positive integer: "))
#             if number<0:
#                 print("Error: Enter Positive integer.")
#             else:
#                 return number
#                 break
#         except:
#             print("Error: Enter Positive integer.")
#
# def fact(number):
#     if number>0:
#         check=number-1
#         result=number
#         while check!=0:
#             result=result*check
#             check-=1
#     elif number==0:
#         result=1
#     else:
#         result="Error"
#
#     return result
#
# main()
#
# #Q30
# def main():
#     firstname,lastname,salary=input_salary()
#     newsalary=new_salary(salary)
#     output_salary(firstname,lastname,newsalary)
#
# def input_salary():
#     first_name=input("Enter first name: ")
#     last_name=input("Enter last name: ")
#     while True:
#         try:
#             salary_current=float(input("Enter current salary: "))
#         except:
#             print("Enter correct salary value")
#         if salary_current<0:
#             print("Salary cannot be negative")
#         else:
#             break
#     return first_name,last_name,salary_current
#
# def new_salary(salary_current):
#     if salary_current<40000:
#         salary_new=1.05*salary_current
#     else:
#         salary_new=40000+2000+(1.02*(salary_current-40000))
#     return salary_new
#
# def output_salary(first_name,last_name,salary_new):
#     print("New salary for {0:} {1:}: ${2:.2f}".format(first_name.title(),
#     last_name.title(),salary_new))
#
# main()
