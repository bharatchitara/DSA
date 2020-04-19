#DSA-Exer-18

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    minimun=num_list[start_index]
    index=start_index
    for i in range(start_index+1,len(num_list)):
        if(num_list[i]<minimun):
            minimum = num_list[i]
            index=i
    return index

    
#Pass different values to the function and test your program
num_list=[1,2,3,4,5,6,1]
start_index=1
print("Index of the next minimum element is", find_next_min(num_list,start_index))