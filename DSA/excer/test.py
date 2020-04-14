# #PF-Exer-22
# 
# def generate_ticket(airline,source,destination,no_of_passengers):
#     ticket_number_list=[]
#     
#     source= source[0:3]
#     destination= destination[0:3]
#     
#     x=no_of_passengers-5
#     
#     if(no_of_passengers>5):
#         count=106
#         while(x>0):
#             ticket_number_list.append(airline)
#             ticket_number_list.append(source)
#             ticket_number_list.append(destination)
#             ticket_number_list.append(count)
#             count+=1
#             x=x-1
#     elif(no_of_passengers<5):
#         count=101
#         while(no_of_passengers>0):
#             ticket_number_list.append(airline)
#             ticket_number_list.append(source)
#             ticket_number_list.append(destination)
#             ticket_number_list.append(count)
#             count+=1
#             no_of_passengers+=1
#     #Use the below return statement wherever applicable
#     return ticket_number_list
# 
# #Provide different values for airline,source,destination,no_of_passengers and test your program
# print(generate_ticket("AI","Bangalore","London",7))




class Customer:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
class Mobile:
    def __init__(self,brand):
        self.brand=brand
    def unlock(self,cover):
        cover.color="yellow"
class Cover:
    def __init__(self):
        self.color="red"
Customer("Cus1",Mobile("Apple")).mobile.unlock(Cover())
print(Cover().color)