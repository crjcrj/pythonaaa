from typing import List
class Quchong:
    def remove(self,nums:List,count:int):
        count=1
        fast=1
        slow=0
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                count+=1
                if count==2:
                    slow+=1
                    nums[slow] = nums[fast]
                else:
                    fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
                count=1
                fast+=1
        return slow+1
