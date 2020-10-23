from typing import List
def count(nums:List):
    max_len=max(nums)
    res=[0]*(max_len+1)
    for i in range(len(nums)):
            res[nums[i]]+=1
    ilist=[]
    for i in range(len(res)):
        for _ in range(res[i]):
            ilist.append(i)
    return ilist
t=[9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]
print(count(t))





