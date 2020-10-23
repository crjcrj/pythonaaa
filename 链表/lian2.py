class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
class Linklist:
    def __init__(self):
        self.head=None
        self.tail= None
        self.size=0
    def get(self,index):
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr
    # 添加
    def insert(self,index,data):
        new_data=Node(data)
        if index<0 or index>self.size :
            return "错误"
        if self.size==0:
            self.head=new_data
            self.tail=new_data
        elif index==0:
            new_data.next=self.head
            self.head=new_data
        elif index==self.size:
            self.tail.next=new_data
            self.tail=new_data
        else:
            prev=self.get(index-1)
            new_data.next=prev.next
            prev.next=new_data
        self.size +=1
    # 删除
    def delete(self,index):
        if index<0 or index>=self.size:
            return "cuowu"
        if index==0:
            remove=self.head
            self.head=self.head.next
            remove=None
        elif index==self.size-1:
            prev=self.get(index-1)
            prev.next=None
            self.tail=prev
        else:
            prve=self.get(index-1)
            prve.next=prve.next.next
        self.size -=1
    # 翻转
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            none_data=curr.next
            curr.next=prev
            prev=curr
            curr=none_data
        return curr
    # 输出
    def __repr__(self):
        curr=self.head
        str_repr=""
        while curr:
            str_repr+="{}-->".format(curr)
            curr=curr.next
        return str_repr+"end"
