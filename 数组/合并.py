# from typing import List
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
#
# def he(l1:List,l2:List):
#     dummy=Node(0)
#     curr=dummy
#     while l1 or l2:
#         if l1 is None:
#             curr.next=l2
#             break
#         if l2 is None:
#             curr.next=l1
#         if l1.data < l2.data:
#             curr.next = Node(l1.data)
#             l1 = l1.next
#         else:
#             curr.next = Node(l2.data)
#             l2 = l2.next
#         curr = curr.next
#
# def he2(l1:List,l2:List):
#     dummy=Node(0)
#     curr=dummy
#     while l1 and l2:
#         if l1.data < l2.data:
#             curr.next = Node(l1.data)
#             l1 = l1.next
#         else:
#             curr.next = Node(l2.data)
#             l2 = l2.next
#         if l1 is None:
#             curr.next=l2
#         if l2 is None:
#             curr.next=l1
#         curr = curr.next
#
# 用数组创建栈
class Stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    # 压栈
    def push(self,data):
        curr=self.stack.append(data)
        self.size+=1
    # 弹栈
    def pop(self):
        if self.stack is None:
            return "yuejie"
        else:
            temp=self.stack.pop()
            self.size-=1
        return temp
    def peek(self):
        if self.stack:
            return self.stack[-1]
# 用链表创建栈
class Node():
    def __init__(self,data):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    # 压栈
    def push(self,data):
        new_data=Node(data)




