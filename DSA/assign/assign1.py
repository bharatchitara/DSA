#DSA-Assgn-1
 
def merge_list(list1, list2):
    merged_data=""
    resultant_data=""
     
    list2 = list2[::-1]
     
    for i in range(0,len(list1)):
        if(list2[i]==None ):
            merged_data=str(list1[i])
            merged_data+=" "
            resultant_data+=merged_data
            #resultant_data.split('""')
             
        elif(list1[i]==None):
            merged_data=str(list2[i])
            merged_data+=" "
            resultant_data+=merged_data
           # resultant_data.split('""')
             
        elif(len(list1)==len(list2)):
            merged_data=str(list1[i])+str(list2[i])
            
            merged_data+=" "
            resultant_data+= merged_data
            #resultant_data.split('""')
     
    return str(resultant_data)
    #write your logic here
 
 
#Provide different values for the variables and test your program
list1=[None,'a']
list2=[None,"an"]
merged_data=merge_list(list1,list2)
print(merged_data)


