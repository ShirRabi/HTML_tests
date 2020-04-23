def compare(current_data_times,current_data_tags,db_data):
#inputs: current_data_times- list of the repititions of the HTML tags of input website
#current_data_tags-list of the HTML tags of input website
#db_data- type list. A table of expected elements and repititions, taken from DB.
#purpose: compares between table from DB to input lists and prints the differences
    for line in db_data:
        flag=0
        ind=0
        for tag in current_data_tags:
            temp=line[1].split()[0] #clear spaces
            if temp==tag:
                flag=1
                print(str(temp) + " expected " + str(line[0]) + " found " + str(current_data_times[ind]))
                break
            ind += 1
        if flag==0:
            print(str(temp[0])+" expected "+str(line[0])+" found "+"0")



