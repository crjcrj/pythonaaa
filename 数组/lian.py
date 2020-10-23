class Array:
    def __init__(self,capacity):
        self.array=[None]*capacity
        self.size=0
    def insert(self,index,element):
        if index<0 or index>self.size:
            return "cuowu"
        if index>len(self.array)-1:
            self.addarrary()
        for i in range(self.size-1,index-1,-1):
            self.array[i+1]=self.array[i]
        self.array[index]=element
        self.size+=1
    def remove(self,index):
        if index<0 or index>=self.size:
            return "cuowu"
        for i in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size-=1

    def addarrary(self):
        new_array=[None]*len(self.array)*2
        for i in range(self.size):
            self.array[i]=new_array[i]
        self.array=new_array


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
def is_cirse(head:Node):
    fast=head
    slow=head
    if fast or fast.next:
        fast=fast.next.next
        slow=slow.next






