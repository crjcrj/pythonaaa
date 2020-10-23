from pprint import pformat
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return "Node({})".format(self.data)
class Tree:
    def __init__(self):
        self.root= None

    def get(self,data):
        node=Node(data)
        if self.root is None:
            self.root=node
        else:
            temp=[self.root]
            while True:
                pop_node=temp.pop(0)
                if pop_node.left is None:
                    pop_node.left=node
                    return
                elif pop_node.right is None:
                    pop_node.right=node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    # 二叉树父级
    def parent(self,item):
        if self.root==item:
            return
        temp=[self.root]
        while temp:
            pop_node=temp.pop(0)
            if pop_node.left:
                if pop_node.val==item:
                    return pop_node
                else:
                    temp.append(pop_node.left)
            if pop_node.right:
                if pop_node.val==item:
                    return pop_node
                else:
                    temp.append(pop_node.right)


if __name__ == '__main__':
    t = Tree()
    t.get(1)
    t.get(2)
    t.get(3)
    t.get(6)
    t.get(5)
    t.get(6)
    t.get(7)

    print(t.root.left.left)

