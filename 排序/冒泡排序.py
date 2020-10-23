from typing import List
import random
from Randlist import Randlist
def sort(nums:List):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

print(sort(Randlist.randlist(10)))
