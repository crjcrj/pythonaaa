from typing import List
class Quchong:
    def remove(self,nums:List):
        fast=1
        slow=0
        while fast<len(nums):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]
                fast+=1
            else:
                fast+=1
        return slow+1
class  Yidongling:
    def yi(self,nums:List):
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]==0:
                fast+=1
            else:
                nums[slow]=nums[fast]
                fast+=1
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0


class yidong:
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
        return slow


