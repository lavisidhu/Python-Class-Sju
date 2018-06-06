def main():
    temp=txt_list("Cities.txt")
    city_list=[]

    for city in temp:
        city=city.split(',')
        perc_inc=(float(city[3])-float(city[2]))/(float(city[2]))

        city.append(perc_inc)
        # city.append("{0:.2%}".format(perc_inc))
        city_list.append(city)
    city_list.sort(key=lambda x: x[4],reverse=True)

    for city in city_list:
        city[4]=str(round(city[4]*100,2))
        del city[1:4]

    write_file(city_list,'cities_new.txt')

def txt_list(filename):
    infile=open(filename,"r")
    list_of_text=[]
    for line in infile:
        line=line.rstrip()
        list_of_text.append(line)
    return list_of_text

def write_file(list_name,newfile):
    outfile=open(newfile,'w')
    for item in list_name:
        line=",".join(item)
        outfile.write(line+'\n')

main()
