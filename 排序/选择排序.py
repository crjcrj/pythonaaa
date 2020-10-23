from typing import List
from Randlist import Randlist

def select(nums:List):
    for i in range(len(nums)):
        minindex=i
        for j in range(i+1,len(nums)):# 内层循环找极致的索引值
            if nums[minindex]>nums[j]:
                minindex=j
        nums[i],nums[minindex]=nums[minindex],nums[i]
    return nums
a=Randlist.randlist(10)
# print(a)
print(select(a))