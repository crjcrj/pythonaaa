from typing import List
# def minlist(ilist:List,s:int):
    # sumlist=0
    # newlist=[]
    # if sumlist>=s:
    #     return newlist
    # else:
    #     for right in range(1,len(ilist)):
    #         targar=ilist[right]
    #         for left in range(0,right):
    #             if ilist[left]>targar:
    #                 ilist[left+1:right+1]=ilist[left:right]
    #                 ilist[left]=targar
    #                 sumlist+=left
    #                 newlist.append(left)

def minlist(nums:List,s:int):
    left,sums,res=0,0,float('inf')
    for right in range(len(nums)):
        sums+=nums[right]
        while sums >=s:
            if right - left +1<res:
                res=right - left +1
            sums-=nums[left]
            left+=1
    return res
if __name__ == '__main__':
    t=[2,3,1,2,4,3]
    print(minlist(t,7))


