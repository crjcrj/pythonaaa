class Node:
    def __init__(self,data,parent):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None

    def __repr__(self):
        pass


def get_max(left):
    pass


def is_right(node):
    pass


class Bst:
    def __init__(self):
        self.root=None
    def remove(self,data):
        if self.root is None:
            raise IndexError
        else:
            node=self.root
            while node:
                if node.left is None and node.right is None:
                    self._regrin_nodes(node,Node)
                if node.left is None:
                    self._regrin_nodes(node,node.right)
                if node.right is None:
                    self._regrin_nodes(node,node.left)
                else:
                    temp=get_max(node.left)
                    self.remove(temp.data)
                    node.data=temp.data


    def _regrin_nodes(self, node,children):
        if children is not None:
            node.parent=children
        if node is not None:
            if is_right(node):
                node.parent.right=children
            else:
                node.parent.left=children
        else:
            self.root=children


