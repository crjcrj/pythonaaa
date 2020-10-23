class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
def remove(head,val):
    dummy=Node(0)
    dummy.next=head
    curr=dummy
    while curr.next:
        if curr.next.val==val:
            temp=curr.next
            curr.next=curr.next.next
            temp=None
        else:
            curr=curr.next
        return dummy.next

def huan(head):
    dummy=Node(0)
    dummy.next=head
    prev=dummy
    while prev.next and prev.next.next:
        fast=prev.next.next
        slow=prev.next
        # 换位置
        prev.next=fast
        slow.next=fast.next
        fast.next=slow
        # 调整prev位置
        prev=prev.next.next
    return dummy.next






def hebing(self,l1:Node,l2:Node):

    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = Node(l1.val)
            l1 = l1.next
        else:
            curr.next = Node(l2.val)
            l2 = l2.next
        curr = curr.next
    if l1 is None:
        curr.next = l2

    if l2 is None:
        curr.next = l1

    return dummy.next

