from typing import List

def merge(left, right):
    res=[]
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    if right:
        res.extend(right)
    return res

def mergesort(nums:List):
    if len(nums)<=1:
        return nums
    else:
        mid=len(nums)//2
        left,right=nums[0:mid],nums[mid:]
        return merge2(mergesort(left),mergesort(right))


def merge2(left,right):
    res=[]
    m,n=0,0
    while m<len(left) and n<len(right):
        if left[m] < right[n]:
            res.append(left[m])
            m += 1
        else:
            res.append(right[n])
            n += 1
    res.extend(left[m:])
    res.extend(right[n:])
    return res
t=[2,4,3,1,5,9,7,8]
print(mergesort(t))