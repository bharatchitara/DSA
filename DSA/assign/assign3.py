#DSA-Assgn-3

def check_double(list1,list2):
    new_list=[]
    updated=[]
    final=[]
    for i in range(0,len(list1)):
        x=int(list1[i])*2
        new_list.append(x)
    #write your logic here
    for i in range(0,len(new_list)):
        for j in range(0,len(list2)):
            if(list2[j]==new_list[i]):
                updated.append(new_list[i])
                
                
    for i in range(0,len(updated)):
        x=int(updated[i])//2
        final.append(x)
    return final
    

#Provide different values for the variables and test your program
list1=[11, 8,23,7,25, 15]
list2=[6, 33, 50,31, 46, 78, 16,34]
print(check_double(list1, list2))