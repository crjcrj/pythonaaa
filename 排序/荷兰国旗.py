from typing import List

def sortColor(nums):
    a = c = 0
    b = len(nums) - 1
    while c <= b:
        if nums[c] == 0:
            nums[c],nums[a] = nums[a],nums[c]
            c += 1
            a += 1
        elif nums[c] == 2:
            nums[c],nums[b] = nums[b],nums[c]
            b -= 1
        else:
            c += 1