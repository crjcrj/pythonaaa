def get_max_comment_divisor(a:int,b:int):
    big=max(a,b)
    small=min(a,b)
    if big % small==0:
        return small
    for i in range(small // 2 ,1,-1):
        if big % i ==0 and small % i ==0:
            return i
print(get_max_comment_divisor(20,10))
# 辗转相除法
def get_max_comment_divisor2(a:int,b:int):
    big=max(a,b)
    small=min(a,b)
    c=big % small
    if big % c==0:
        return small
    return get_max_comment_divisor2(small,c)
print(get_max_comment_divisor(20,10))#取余比较麻烦
# 更相减损术
# 相差较大减法会用很多次
def get_max_comment_divisor3(a:int,b:int):
    big=max(a,b)
    small=min(a,b)
    if big%2==0 and small%2==0:
        big=big/2
        small=small/2
    c=big-small
    if small==c:
        return small
    return get_max_comment_divisor2(small,c)
print(get_max_comment_divisor(20,10))

