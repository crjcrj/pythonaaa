# # 单指针快排
from typing import List
#
#
# def messrge(nums, start, end):
#     pivort=nums[start]
#     mark=start
#     for i in range(start+1,end+1):
#         if nums[i]<pivort:
#             mark+=1
#             nums[mark],nums[i]=nums[i],nums[mark]
#     nums[start]=nums[mark]
#     nums[mark]=pivort
#     return mark
# def quicksort(nums:List,start,end):
#     if start>end:
#         return
#     mid=messrge(nums,start,end)
#     quicksort(nums,start,mid-1)
#     quicksort(nums,mid+1,end)
#     return nums


# 计数排序
# def count(nums:List):
#     max_len=max(nums)
#     res=[0]*(max_len+1)
#     for i in range(len(nums)):
#         res[nums[i]]+=1
#     ilist=[]
#     for i in range(len(res)):
#         for _ in range(res[i]):
#             ilist+=[i]
#     return ilist
#
# t=[0,8,7,7,6,1,2,2,3,3,4,4,4,4,5,6,7]
# print(count(t))
# 字典树
class Node:
    def __init__(self):
        self.data={}
        self.is_word=False
    def __repr__(self):
        return str(self.data)
class  Tire:
    def __init__(self):
        self.root=None
    def insert(self,word):
        node=self.root
        for char in word:
            child=node.data.get(char)
            if child is None:
                node.data[char]=Node()
            node=node.data[char]
        node.is_word=True

