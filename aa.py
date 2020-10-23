from typing import List
class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=None

    def __repr__(self):
        return "Node({})".format(self.data)
class linklist():
    def __init__(self):
        self.head=None
    # 表头添加
    def insert_head(self,data):
        new_data=Node(data)
        if self.head:
            new_data.next=self.head
        self.head=new_data
    # 标尾添加
    def app(self,data):
        temp=self.head
        if self.head:
            while temp.next:
                temp=temp.next
            temp.next=Node(data)
        else:
            self.insert_head(data)
    # 中间插入
    def insert(self,i,data):
        if self.head is None:
            self.insert_head(data)
        elif i==1 :
            self.insert_head(data)
        else:
            temp=self.head
            j=1
            pre=temp
            while j<i:
                pre=temp
                temp=temp.next
                j+=1
            none=Node(data)
            pre.next=none
            none.next=temp
    # 输出
    def __repr__(self):
        curr=self.head
        str_repr=""
        while curr:
            str_repr+="{} -->".format(curr)
            curr=curr.next
        return str_repr + "end"
    # 删除头结点
    def delect_head(self):
        if self.head:
            self.head=self.head.next
    # 删除尾部结点
    def delect_tail(self):
        temp=self.head
        if temp:
            if temp.next is None:
                temp=None
            else:
                while temp.next.next:
                    temp=temp.next
                temp.next=None
    # 列表
    def llist(self,object : List):
        self.head=Node(object[0])
        temp=self.head
        for i in  object[1:]:
            none=Node(i)
            temp.next=none
            temp=temp.next



ll=linklist()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.app(4)
ll.insert(2,5)
print(ll)




