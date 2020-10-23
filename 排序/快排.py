from typing import List


def swap(ilist:List, p, q):
    ilist[p],ilist[q]=ilist[q],ilist[p]

def parsion(ilist:List, start, end):
    pivor=ilist[start]
    p=start+1
    q=end
    while p<=q:
        while p<=q and ilist[p]<pivor:
            p+= 1
        while p<=q and ilist[q]>pivor:
            q-=1
        if p<q:
            swap(ilist,p,q)
    swap(ilist,start,q)
    return q

def quicksort(ilist:List,start,end):
    if start>=end:
        return
    mid=parsion(ilist,start,end)
    quicksort(ilist,start,mid-1)
    quicksort(ilist,mid+1,end)
    return ilist
t=[4,3,2,9,6,5,7]
print(quicksort(t,0,len(t)-1))