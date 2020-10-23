from typing import List
def insertsort(ilist:List):
    if len(ilist)<2:
        return ilist
    for right in range(1,len(ilist)):
        targar=ilist[right]
        for left in range(0,right):
            if ilist[left]>targar:
                ilist[left+1:right+1]=ilist[left:right]
                ilist[left]=targar
                break
    return ilist
class Node:
    def __init__(self, val):
        self.val=val
        self.next=Node
    def __repr__(self):
        return
def insertlist(head:Node):
    dummy=Node(0)
    pre=dummy
    curr=head
    while curr:
        temp=curr.next
        while pre.next and pre.next.val<curr.val:
            pre=pre.next
        curr.next=pre.next
        pre.next=curr
        curr=temp
        pre=dummy
    return dummy.next

