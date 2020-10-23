# def count(int):
#     count=0
#     while int!=0:
#         int=int&int-1
#         count+=1
#     return count
# print(count(11))
from typing import List
def shu(a:List):
    res=0
    for i in a:
        res=res^i
    return res
print(shu([4,1,2,1,2]))
