#DSA-Assgn-14
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def check_numbers(number_queue):
    #write your logic here  
    solution_queue1 = Queue(number_queue.get_max_size())
    lst =[]
    l =[]
    
    while(not number_queue.is_empty()):
        lst.append(number_queue.dequeue())
    
    
    flag=0
    for i in range(len(lst)):
        j=1
        flag=0
        while(lst[i]%j==0 and j<11):
            j+=1
            flag+=1
            
        if(flag==10):
            l.append(lst[i])
    
    for index in l:
        solution_queue1.enqueue(index)
               

    return solution_queue1

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
#number_queue.enqueue(2501)

check_numbers(number_queue)
                                                    