# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def is_circle(head:Node):
#     fast=head
#     slow=head
#     while fast and fast.next:
#         fast=fast.next.next
#         slow=slow.next
#         if fast==slow:
#             return True
#     return False
# if __name__=='__main__':
#     node1=Node(1)
#     node2=Node(2)
#     node3=Node(3)
#     node4=Node(4)
#     node5=Node(5)
#
#     node1.next=node2
#     node2.next=node3
#     node3.next=node4
#     node4.next=node5
#     node5.next=node3
    # print(is_circle(node1))


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
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
    return slow
if __name__=='__main__':
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    node5=Node(5)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    # node5.next=node3
    print(is_circle(node1))