class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Ll:
    def __init__(self):
        self.head=None
    def print(self):
        if self.head is None:print("LinkedList is empty.")
        itr=self.head
        st=''
        while itr:
           st+=str(itr.data)+"-->" if itr.next else str(itr.data)
           

           itr=itr.next 
        print(st)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        print(count)
    def insert_at_start(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head==None:
            n=Node(data,None)
            self.head=n
        itr=self.head
        while itr.next:
            itr=itr.next
       
        itr.next=Node(data,None)
    def insert_at(self,index,data):
     
        if index==0:
            self.insert_at_start(data)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
                break             


            itr=itr.next
            count+=1
        itr.next=Node(data,None)
        
    def remove(self,index):
       
        

        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count==index-1:
               itr.next=itr.next.next
            itr=itr.next
            count+=1
    


    def insert_values(self,list):
        self.head=None
        for data in list:
            self.insert_at_end(data)
if __name__=="__main__":
    j=Ll()
    
    j.insert_at_start(372)
    j.insert_at_start(32)
    j.insert_at_end(992)
    j.print()
    j.remove(1)
    j.print()
    j.insert_values(["jojo","miko",3,4])
    j.print()