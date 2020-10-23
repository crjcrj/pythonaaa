class  Queue:
    def __init__(self):

        self.array=[]
        self.size=0

    def __str__(self):
        return  str(self.array)
    def enqueue(self,data):
        self.array.append(data)
        self.size += 1
        self.happy_up()
    def dequeue(self):
        temp=self.array[0]
        self.array=self.array[1:]
        self.size -= 1
        self.happy_down()
        return temp

    def happy_down(self):
        pass

    def happy_up(self):
        child_index=self.size-1
        parent_index=(child_index-1)>>1
        new=self.array[child_index]
        while child_index>0 and new>self.array[parent_index]:
            self.array[child_index]=self.array[parent_index]
            child_index=parent_index
            parent_index=(child_index-1)>>1
        self.array[child_index]=new
ll=Queue()
ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)
ll.enqueue(4)
print(ll)

