from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.val = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return pformat({"%s" % (self.val): (self.left, self.right)}, indent=1)


class Tree:
    def __init__(self):
        self.root = None

    def __insert(self, value):
        new_node = Node(value, None)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if new_node.val < parent_node.val:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node
    def __repr__(self):
        return str(self.root)
    def insert2(self,*vals):
        for val in vals:
            self.__insert(val)
        return self

    def is_empty(self):
        if self.root is None:  # self.node is None
            return True
        else:
            return False

    def search(self,val):
        if self.root is None:
            raise IndexError
        else:
            node=self.root
            while node and node.val!=val:
                if val<node.val:
                    node=node.left
                elif val >node.val:
                    node=node.right
            return node


    def remove(self,val):
        node=self.search(val)
        if node is  not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node,None)
            elif node.left is None:
                self.__reassign_nodes(node,node.right)
            elif node.right is None:
                self.__reassign_nodes(node,node.left)
            else:
                temp=self.get_max(node.left)
                self.remove(temp.val)
                node.val=temp.val

    def __reassign_nodes(self,node,new_children):
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

    #   前序 (递归）
    def presort(self,node):
        if not node:
            return None
        print(node.data)
        self.presort(node.left)
        self.presort(node.right)

    def preorder(self, node):
        stack = [node]
        while len(stack) > 0:
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    # def in_order_stack(self,node):
    #     stack=[]
    #     while node or len(stack)>0:
    #         while node:
    #             stack.append(node)
    #             node=node.left
    #         if len(stack)>0:
    #             node=stack.pop()
    #             print(node.val)
    #             node=node.right
    def post_order_stasck(self,node):
        if node is None:
            return False
        stack1=[]
        stack2=[]
        stack1.append(node)
        while stack1:
            stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack2.append(node.right)
            stack2.append(node)
            while stack2:
                print(stack2.pop().data)
    # 层序遍历
    def leve_order(self,node):
        if self.root is None:
            raise IndexError
        else:
            queue=[node]
            while queue:
                temp=queue.pop(0)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
                print(temp.data)






bst=Tree().insert2(8,3,1,6,4,7)
print(bst)
