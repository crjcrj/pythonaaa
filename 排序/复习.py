from typing import List


# def merge(left, right):
#     res=[]
#     while left and right:
#         if left[0]<right[0]:
#             res.append(left.pop(0))
#         else:
#             res.append(right.pop(0))
#     if left:
#         res.extend(left)
#     if right:
#         res.extend(right)
#     return res
# def merge2(left,right):
#     m,n=0,0
#     res=[]
#     while m<len(left) and n<len(right):
#         if left[m]<right[n]:
#             res.append(left[m])
#             m+=1
#
#         else:
#             res.append(right[n])
#             n+=1
#     res.extend(left[m:])
#     res.extend(right[n:])
#     return res
#
# def sort(nums:List):
#     if len(nums)<=1:
#         return nums
#     else:
#         mid=len(nums)//2
#         left,right=nums[0:mid],nums[mid:]
#         return merge2(sort(left),sort(right))
# t=[4,3,5,8,7,9]
# print(sort(t))
# def swap(nums,p, q):
#     nums[p],nums[q]=nums[q],nums[p]
#
#
# def mersge(nums, start, end):
#     pivor=nums[start]
#     p=start+1
#     q=end
#     while p<q:
#         while p<=q and nums[p]<pivor:
#             p+=1
#         while p<=q and nums[q]>pivor:
#             q-=1
#         if p<q:
#             swap(nums,p,q)
#     swap(nums,start,q)
#     return q
#
#
# def quicksort(nums:List,start,end):
#     if start>end:
#         return
#     mid=mersge(nums,start,end)
#     quicksort(nums,start,mid-1)
#     quicksort(nums,mid+1,end)
#     return nums
# t=[4,3,5,8,7,9]
# print(quicksort(t,0,len(t)-1))
def concat(nums:List):
    fast=1
    slow=0
    while fast<len(nums):
        if nums[fast]==nums[slow]:
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]
            fast+=1
    return nums[0:slow+1]
t=[2,3,3,4,5]
print(concat(t))

