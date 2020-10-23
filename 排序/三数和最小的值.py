# 16
# def threeSumClose(nums,target):
#     nums.sort()
#     res = nums[0] + nums[1] + nums[2]
#     closest = abs(nums[0] + nums[1] + nums[2] - target)
#     for i in range(len(nums) - 2):
#         left = i + 1
#         right = len(nums) - 1
#
#         while left < right:
#             threesum = nums[i] + nums[left] + nums[right]
#             if abs(target - threesum) < closest:
#                 res = threesum
#                 closest = abs(target - threesum)
#             if threesum < target:
#                 left += 1
#             elif threesum > target:
#                 right -= 1
#             else:
#                 return threesum
#     return res
# print(threeSumClose([0,2,1,-3],3))
from typing import List
# def three(nums:List):
#     nums.sort()
#     count=0
#     for i in range(2,len(nums)):
#         left=0
#         right=i-1
#         while left<right:
#             if nums[left]+nums[right]>nums[i]:
#                 count+=right-left
#                 right-=1
#             else:
#                 left += 1
#     return count
# t=[2,2,3,4]
# print(three(t))
def three(nums:List):
    nums.sort()
    count=0
    for i in range(1,len(nums)):
        left=i+1
        right=len(nums)-1
        while left<right:
            if nums[i]+nums[left]>nums[right]:
                count+=right-left
                right-=1
            else:
                left += 1
    return count
t=[2,2,3,4]
print(three(t))
