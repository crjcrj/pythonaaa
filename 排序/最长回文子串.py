def centerspread(strs:str,left:int,right:int):
    i=left
    j=right
    while i>0 and j<len(strs):
        if strs[i]==strs[j]:
            i-=1
            j+=1
        else:
            break
    return strs[i+1:j]

def longest(strs:str):
    length=len(strs)
    if length<2:
        return strs
    maxlen=1
    res=strs[0]
    for i in range(length-1):
        odd=centerspread(strs,i,i)#奇数
        even=centerspread(strs,i,i+1)#偶数
        if len(odd)>len(even):
            maxstr=odd
        else:
            maxstr = even
        if len(maxstr)>maxlen:
            maxlen=len(maxstr)
            res=maxstr
    return res
if __name__ == '__main__':
    strs='1001000100001'
    print(longest(strs))
