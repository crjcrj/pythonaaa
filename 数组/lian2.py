from typing import List
class He:
    def sum(self,nums:List,val:int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==val:
                    return i,j




class He2:
    def sum2(self,nums:List,val:int):
        sit={}
        for i in range(len(nums)):
            temp=val-nums[i]
            if temp in str:
                return
            else:
                sit[nums[i]]=i



class He3:
    def sum3(self,nums:List,val:int):
        fast=0
        tail=len(nums)-1