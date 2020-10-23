from typing import List
from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data=data
        self.left=None
        self.right=None
        self.parent=parent
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)
class Tree:
    def __init__(self):
        self.root=None
    def is_empty(self):
        if self.root is None:
            return  True
        return False
    def insert(self,data):
        node=Node(data,None)
        if self.root is None:
            self.root=node
        else:
            temp=self.root
            while True:
                if data<temp.data:
                    if temp.left is None:
                        temp.left=node
                        break
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp=temp.right
                        break
                    else:
                        temp=temp.right
            node.parent=temp
    def __repr__(self):
        return str(self.root)
    def insert2(self,vals):
        for i in vals:
            self.insert(i)
        return self
    def search(self,val):
        if self.root is None:
            raise IndexError
        else:
            node=self.root
            while node and node.data!=val:
                if val<node.data:
                    node=node.left
                else:
                    node=node.right
    def remove(self,val):
        if self.root is None:
            raise  IndexError
        else:
            node=self.search(val)
            if node is not None:
                if node.left is None and node.right is None:
                    self.__ressign_nodes(node,None)
                elif node.left is None:
                    self.__ressign_nodes(node,node.right)
                elif node.right is None:
                    self.__ressign_nodes(node,node.left)
                else:
                    temp=self._max(node.left)
                    self.remove(temp.val)
                    node.val=temp.val


    def __ressign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent=node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right=new_children
            else:
                node.parent.left=new_children
        else:
            self.root=new_children




    def _max(self, left):
        pass


