def sum(a:int,b:int):
    c=a^b
    count=0
    while c:
        if c&1:
            count+=1
        c=c>>1
    return count