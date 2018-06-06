def main():
    temp=txt_list("ALE.txt")
    team_list=[]

    for team in temp:
        team=team.split(',')
        perc_won=round(int(team[1])/(int(team[1])+int(team[2])),3)
        team.append(perc_won)
        team_list.append(team)
    team_list.sort(key=lambda x: x[3],reverse=True)
    for team in team_list:
        team[3]=str(team[3])

    write_file(team_list,'ale_new.txt')

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
