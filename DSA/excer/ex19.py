#DSA-Exer-19

def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    num_list[first_index],num_list[second_index]= num_list[second_index],num_list[first_index]


def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    minimun=num_list[start_index]
    index=start_index
    for i in range(start_index+1,len(num_list)):
        if(num_list[i]<minimun):
            minimum = num_list[i]
            index=i
    return index

def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    #count=0
    for i in range(0,len(num_list)-1):
        min = find_next_min(num_list, i)
        swap(num_list, i, min)
     #   count+=1


#Pass different values to the function and test your program
num_list=[13, 67, 23, 88, 10, 4, 55, 2]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)