# # 用数组创建队列
# class  Queue:
#     def __init__(self):
#         self.entirse=[]
#         self.size=0
#     def enqueue(self,data):
#         self.entirse.append(data)
#         self.size += 1
#     def dequeue(self):
#         temp=self.entirse[0]
#         self.entirse=self.entirse[1:]
#         self.size -= 1
#         return temp
#     def get(self,index):
#         return self.entirse[index]
#     def set(self,index,data):
#         self.entirse[index]=data
#     def reverse(self):
#         return self.entirse[::-1]
#     def __str__(self):
#         return  str(self.entirse)
#







# 链表创建队列
class Node:
    def __init__(self,data):
       self.data=data
       self.next=None

    def __repr__(self):
        return "Node({})".format(self.data)
class Listqueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def enqueue(self,data):
        none=Node(data)
        if self.size==0:
            self.head=none
            self.tail=none
        else:
            self.tail.next=none
            self.tail=none
        self.size +=1
    def dequeue(self):
        if self.size==0:
            return "yuejie"
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.size -=1
    def __repr__(self):
        curr=self.head
        str_r=""
        while curr:
            str_r+="{} -->".format(curr)
            curr=curr.next
        return str_r +"end"
    def get(self,index):
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr






ll= Listqueue()

ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)

print(ll)


