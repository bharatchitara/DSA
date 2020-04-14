#DSA-Exer-1
flag=0
def update_mark_list(mark_list, new_element, pos):
    #Write your logic here
    if(len(mark_list)>pos):
        mark_list.insert(pos,new_element)
        flag=1
        return mark_list
    else:
        return False

def find_mark(mark_list,pos1,pos2):
    if(len(mark_list)>pos1 and len(mark_list)>pos2 and flag==1):
        print(mark_list[pos1])
        print(mark_list[pos2])
    else:
        print( False)
#Provide different values for the variables and test your program
mark_list=[98, 87, 65, 33, 49]
new_element=78
pos=12
pos1=2
pos2=3
print(update_mark_list(mark_list, new_element, pos))
find_mark(mark_list, pos1, pos2)