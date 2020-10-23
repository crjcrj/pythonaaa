from typing import List
from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat("%s"%{(self.data) :(self.left,self.right)},indent=1)





class Tree:
    def __init__(self):
        self.root=None
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def insert(self,data):
        node=Node(data,None)
        if self.root is None:
            self.root=node
        else:
            temp=self.root
            while  True:
                if data<temp.data:
                    if temp.left is None:
                        temp.left=node
                        break
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=node
                        break
                    else:
                        temp=temp.right
            node.parent=temp
    def search(self,data):
        if self.root is None:
            raise IndexError
        else:
            node=self.root
            while node and node.data != data:
                if data<node.data:
                    node=node.left
                else:
                    node=node.right
            return node
    def remove(self,data):
        if self.root is None:
            raise IndexError
        else:
            node=self.search(data)
            while node.parent is not None:
                if node.left is None and node.right is None:
                    self.__ressign_nodes(node,None)
                elif node.left is not None:
                    self.__ressign_nodes(node,node.left)
                elif node.right is not None:
                    self.__ressign_nodes(node,node.right)
                else:
                    temp=self.is_max(node.left)
                    self.remove(temp.data)
                    node.data=temp.data



    def __ressign_nodes(self, node, new_children):
        if new_children is None:
            node.parent=None
        if node is not None:
            if self.is_right(node):
                node.parent.right=new_children
            else:
                node.parent.left=new_children
        self.root=new_children

    def is_max(self, left):
        pass

    def is_right(self,node):
        return node==node.parent.right
