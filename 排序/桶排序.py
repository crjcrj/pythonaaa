from typing import List
def barrel(nums:List):
    min_data=min(nums)
    max_data=max(nums)
    d=max_data-min_data
     # 初始化通
    bucket_num=len(nums)#桶的个数
    count_list=[]  #桶空间
    for i in range(bucket_num):
        count_list.append([])#造桶

    # 定位元素属于那个桶
    for i in range(len(nums)):
        num=int((nums[i]-min_data)/d)*(bucket_num-1)
        bucket=count_list[num]
        bucket.append(nums[i])
    # 桶内排序
    for i in range(len(count_list)):
        count_list[i].sort()
    # 按顺序输出
    sort_nums=[]
    for sub in count_list:
        for item in sub :
            sort_nums.append(item)
        return  sort_nums
t=[4,7,6,5,4,2,1]
print(barrel(t))