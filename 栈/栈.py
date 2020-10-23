# 元组创建栈
class Stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    def pop(self):
        if self.stack:
            temp=self.stack.pop()
            self.size-=1
        else:
            raise IndexError
        return temp
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return self.size

# ll=Stack()
# ll.push(1)
# ll.push(2)
# print(ll.size)


# 链表创建栈
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
class Stack2:
    def __init__(self):
        self.top=None
        self.size=0
    def push1(self,data):
        none=Node(data)
        if self.top is None:
            self.top=none
        else:
            none.next=self.top
            self.top=none
        self.size+=1
    def pop(self):
        if self.top:
            temp=self.top
            self.top=temp.next
            temp.next=None
            self.size-=1
            return temp
        else:
            return "kong"


