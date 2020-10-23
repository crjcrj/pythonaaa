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
        return pformat({"%s" % (self.data): (self.left, self.right)}, indent=1)
class Bst:
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
            while True:
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
                        temp.right=node
    def insert2(self,*datas):
        for i in datas:
            self.insert(i)
        return self

    def search(self,data):
        if self.root is None:
            raise IndexError
        else:
            temp=self.root
            while temp and temp.data!=data:
                if data<temp.data:
                    temp=temp.left
                else:
                    temp=temp.right
            return temp
    def remove(self,data):
        if self.root is None:
            raise IndexError
        else:
            node=self.search(data)
            if node is not None:
                if node.left is None and node.right is None:
                    self.__ressign_nodes(node,None)
                elif node.left is None:
                    self.__ressign_nodes(node,node.right)
                elif node.right is None:
                    self.__ressign_nodes(node,node.left)
                else:
                    temp=self.get_max(node.left)
                    self.remove(temp.data)
                    node.data=temp.data

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

    def get_max(self, node):
        if node is None:
            self.root=node
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node


    def is_right(self,node):
        return node==node.parent.right
    def __repr__(self):
        return str(self.root)

    # 前序递归
    def presort(self,node):
        if not node:
            return None
        print(node.data)
        self.presort(node.left)
        self.presort(node.right)
    # 中序递归
    def insort(self,node):
        if not node:
            return None
        self.presort(node.left)
        self.presort(node.right)
    # 前序遍历
    def preorder(self,node):
        stack=[node]
        while len(stack)>0:
            print(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node=stack.pop()

bst=Bst()
bst.insert2(8,3,1,6,10)
bst.remove(6)
print(bst)