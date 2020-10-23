from typing import List
class Leve:
    def sum(nums:List):

        def sum2(a: int, b: int):
            c = a ^ b
            count = 0
            while c:
                if c & 1:
                    count += 1
                c = c >> 1
            return count
        size=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                size+=sum2(nums[i],nums[j])
        return size
