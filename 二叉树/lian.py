class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return "Node({})".format(self.data)
# class Tree:
#     def __init__(self):
#         self.root=None
#     def insert(self,data):
#         node=Node(data)
#         if self.root is None:
#             self.root=node
#         else:
#             temp=[self.root]
#             while temp:
#                 pop_node=temp.pop(0)
#                 if pop_node.left is None:
#                     pop_node.left=node
#                 else:
#                     temp.append(pop_node.left)
#                 if pop_node.right is None:
#                     pop_node.right=node
#                 else:
#                     temp.append(pop_node.right)
#     # 查找父级
#     def get(self,val):
#         if self.root==val:
#             return "wu"
#         else:
#             temp=[self.root]
#             while temp:
#                 pop_node=temp.pop(0)
#                 if pop_node.left==val:
#                     return
#                 if pop_node.right==val:
#                     return
#                 else:
#                     temp.append(pop_node.left)
#                     temp.append(pop_node.right)
#                 return pop_node


# 二分搜索树
class Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        node=Node(data)
        if self.root is None:
            self.root=node
        else:
            temp=self.root
            while temp:
                if temp.data<data:
                    if temp.left is None:
                        temp.left=node
                    else:
                        temp=temp.left
                if temp.data>data:
                    if temp.right is None:
                        temp.right=node
                    else:
                        temp=temp.right

    def insert2(self,val):
        if self.root==val:
            return



