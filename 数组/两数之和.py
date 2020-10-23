from typing import List
# class He:
#     def liang(self,nums:List,val:int):
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 while i!=j and nums[i]+nums[j]==val:
#                     return i,j


# 对撞指针
# ll=He()
# print(ll.liang([1,2,3,4,5],9))
# def sum(nums:List,val:int):
#     head=0
#     tail=len(nums)-1
#     while head< tail:
#         sum=nums[head]+nums[tail]
#         if sum==val:
#             print(head,tail)
#             head+=1
#             tail-=1
#         else:
#             if sum<val:
#                 head+=1
#             else:
#                 tail-=1
# 新建字典
# def twosum(nums:List,val:int):
#     sum_t={}
#     for i in range(len(nums)):
#         temp=val-nums[i]
#         if temp in sum_t:
#             return [i,sum_t[temp]]
#         else:
#             sum_t[nums[i]]=i
# 三数之和
def sum(nums:List,val:int):
    nums.sort()
    dic=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        fast=i+1
        end=len(nums)-1

        while fast<end:
            if nums[fast]+nums[end]+nums[i]==val:
                dic.append([nums[fast],nums[end],nums[i]])
                while fast<end and nums[fast]==nums[fast+1]:
                    fast+=1
                while fast<end and nums[end]==nums[end-1]:
                    end-=1
                fast+=1
                end-=1
            elif nums[fast]+nums[end]+nums[i]<val:
                fast+=1
            elif nums[fast]+nums[end]+nums[i]>val:
                end-=1


