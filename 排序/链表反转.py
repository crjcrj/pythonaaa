class Node:
    def __init__(self, val):
        self.val=val
        self.next=Node
    def __repr__(self):
        return "Node({})".format(self.val)
class List1:
    def __init__(self):
        self.head=None
#     def reverse(self):
#         pre=None
#         temp=self.head
#
#         while temp:
#             curr=temp.next
#             temp.next=pre
#             pre=temp
#             temp=curr
#         self.head=pre
from typing import  List
# def reverse(nums:List):
#     l=0
#     r=len(nums)-1
#     while l<r :
#         nums[l],nums[r]=nums[r],nums[l]
#         l+=1
#         r-=1
#     return nums
# t=[1,2,3,4]
# print(t)
# print(reverse(t))
#     def two_reverse(self,head):
#         dummy=Node(0)
#         pre=dummy
#         dummy.next=head
#         while pre.next.next and pre.next:
#             slow=pre.next
#             fast=pre.next.next
#             pre.next=fast
#             slow.next=fast.next
#             fast.next=slow
#             pre=pre.next.next
#         return dummy.next
def sum(nums:List,val:int):
    nums.sort()
    for i in range(len(nums)-2):
        left=i+1
        right=len(nums)-1
        while left<right:
            if nums[i]+nums[left]+nums[right]<val:
                left+=1
            elif nums[i]+nums[left]+nums[right]>val:
                right-=1
            else:
                return [nums[i],nums[left],nums[right]]
t=[1,2,3,4,5,6]
print(sum(t,6))











