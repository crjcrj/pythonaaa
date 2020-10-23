from typing import List
from Randlist import Randlist
def sort(nums:List):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],[nums[j]]
    return nums

def select(nums:List):
    for i in range(len(nums)):
        minindex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minindex]:
                minindex=j
        nums[i],nums[minindex]=nums[minindex],nums[i]
    return nums

