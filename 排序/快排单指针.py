from typing import List


def partion(nums, start, end):
    pivort=nums[start]
    mark=start
    for i in range(start+1,end+1):
        if nums[i]<pivort:
            mark+=1
            nums[i],nums[mark]=nums[mark],nums[i]
        nums[start]=nums[mark]
        nums[mark]=pivort
        return mark



def quicksort(nums:List,start,end):
    mid=partion(nums,start,end)
    quicksort(nums,start,mid-1)
    quicksort(nums,mid+1,end)
    return nums
