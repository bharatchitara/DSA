def merge_sort(num_list):
    low=0
    high=len(num_list)-1
    
    if(low == high):
        return num_list
    else:
        
        mid = len(num_list)//2
        left_list = merge_sort(num_list[:mid])
        right_list = merge_sort(num_list[mid:])
        merged_list = merge(left_list, right_list)
    return merged_list
    
def merge(left_list,right_list):
    i=0
    j=0
    sorted_list=[]
    while(i<len(left_list) and j < len(right_list)):
        if(left_list[i]<right_list[j]):
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    
    
    while(i<len(left_list)):
        sorted_list.append(left_list[i])
        i+=1
        
    while(j<len(right_list)):
        sorted_list.append(right_list[j])
        j+=1
            
    return sorted_list        

num_list=[34,67,8,19,2,23,1,19]
print(num_list)          
sorted_list = merge_sort(num_list)
print(sorted_list)  