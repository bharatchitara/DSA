#DSA-Exer-8
#from excer.ex17 import num_list
                                        
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    
    def get_max_size(self):
        return self.__max_size
    
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

    
def split_queue(num_queue):
    
    queue_list=[]
    #q_list=[]
    
    while(not num_queue.is_empty()):
        data= num_queue.dequeue()
        queue_list.append(data)
    
    for i in queue_list:
        if(i%2!=0):
            q_list0.enqueue(i)
            
        if(i%2==0):
            q_list1.enqueue(i)
            
    #list(odd_queue.display())
    

num_queue=Queue(7)
q_list0 = Queue(num_queue.get_max_size())
q_list1 = Queue(num_queue.get_max_size())
    
num_queue.enqueue(1)
num_queue.enqueue(2)
num_queue.enqueue(3)
num_queue.enqueue(4)
num_queue.enqueue(5)
num_queue.enqueue(6)
num_queue.enqueue(7)

q_list=split_queue(num_queue)
#q_list.display
#print(q_list)
q_list0.display()
q_list1.display()