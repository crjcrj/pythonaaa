class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return
def is_circle(head:Node):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break  
    slow=head
    while slow != fast:
        slow=slow.next
        fast=fast.next
    return fast


