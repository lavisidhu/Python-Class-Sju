def main():
    infile=txt_list("Mileage.txt")
    model_list=[]

    for model in infile:
        model=model.split(",")
        model[1]=float(model[1])
        model_list.append(model)

    model_miles=mileage_calc(model_list)

    output(model_miles)

def txt_list(filename):
    infile=open(filename,"r")
    list_of_text=[]
    for line in infile:
        line=line.rstrip()
        list_of_text.append(line)
    return list_of_text

def mileage_calc(model_list):
    new_list=[]
    model_dict={}
    model_dict1={}
    mileage_dict={}
    sorted_miles=[]

    for model in model_list:
        new_list.append(model[0])

    for model in new_list:
        model_dict[model]=0

    for model in new_list:
        count=new_list.count(model)
        model_dict1[model]=count

    for item in model_list:
        model_dict[item[0]]=round((model_dict[item[0]]+item[1]),2)

    for model in model_dict:
        mileage=round(100/(model_dict[model]/model_dict1[model]),2)
        mileage_dict[model]=mileage
    sorted_miles=list(mileage_dict.items())
    sorted_miles.sort(key=lambda x: x[1],reverse=True)

    return sorted_miles

def output(sorted_miles):
    print("{0:<10} {1:<10}".format("Model","MPG"))
    for model in sorted_miles:
        print("{0:<10} {1:<10}".format(model[0],model[1]))


main()
