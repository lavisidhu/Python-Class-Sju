def main():
    grade_list=[]
    grade_dict={}
    temp=txt_list("Scores.txt")
    scores=[int(x) for x in temp]
    number_grades,average_grades,stdv_grades=stats(scores)
    print("Number of scores:",number_grades)
    print("Average score:",average_grades)
    print("Standard deviation of scores:",stdv_grades)
    for score in scores:
        grade=grade_curve(average_grades,stdv_grades,score)
        grade_list.append(grade)

    for grade in sorted(grade_list):
        count=grade_list.count(grade)
        grade_dict[grade]=count
    print("GRADE DISTRIBUTION OF CURVING GRADES.")
    for item in grade_dict:
        print("{}:{}".format(item,grade_dict[item]),end="  ")

def txt_list(filename):
    infile=open(filename,"r")
    list_of_text=[]
    for line in infile:
        line=line.rstrip()
        list_of_text.append(line)
    return list_of_text

def stats(data):
    import statistics
    number=len(data)
    average=round(statistics.mean(data),2)
    stdv=round(statistics.pstdev(data),2)
    return number,average,stdv

def grade_curve(mean,stdv,score):
    if score>=(mean+(1.5*stdv)):
        grade='A'
    else:
        if score>=(mean+(0.5*stdv)):
            grade='B'
        else:
            if score>=(mean-(0.5*stdv)):
                grade='C'
            else:
                if score>=(mean-(1.5*stdv)):
                    grade='D'
                else:
                    grade='F'
    return grade

main()
