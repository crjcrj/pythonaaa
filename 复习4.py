# 数组创建栈
class Stack:
    def __init__(self):
        self.stack=[]
        self.size=None
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    def pop(self):
        if self.stack:
            temp=self.stack.pop()
        else:
            return "越界"
        self.size-=1
        return temp
    def peek(self):
        if self.stack:
            return self.stack[-1]

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
    def push(self,data):
        node=Node(data)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.size+=1
    def pop(self):
        if self.top:
            temp=self.top
            self.top=temp.next
            temp.next=None
            self.size-=1
            return temp


from typing import List
# 去重
class Quchong:
    def yi(self,nums:List):
        fast=1
        slow=0
        while fast<len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow]=nums[fast]
                fast+=1
            else:
                fast+=1


# 移动0
class Yidongling:
    def move(self,nums:List):
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==0:
                fast+=1
            else:
                nums[slow]=nums[fast]
                fast+=1
                slow+=1
# 移动特定值
class Yidongzhi:
    def move(self,nums:List,val:int):
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==val:
                fast+=1
            else:
                nums[slow]=nums[fast]
                fast+=1
                slow+=1
# 最多两个重复
class Quchong2:
    def move2(self,nums:List,count):
        count=1
        fast=1
        slow=0
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                count+=1
                if count==2:
                    slow+=1
                    nums[slow]=nums[fast]
                else:
                    fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
                count=1
                fast+=1



