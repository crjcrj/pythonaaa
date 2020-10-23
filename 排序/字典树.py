class Node:
    def __init__(self):
        self.data={}
        self.is_word=False
    def __repr__(self):
        return str(self.data)


class Tire:
    def __init__(self):
        self.root=Node()
# 插入
    def insert(self,word):
        node=self.root
        for char in word:
            child=node.data.get(char)
            if child is None:
                node.data[char]=Node()
            node=node.data[char]
        node.is_word=True

# 查询
def search(self,word):
    node=self.root
    for char in word:
        node = node.data.get(char)
        if not node:
            return False
    return node.is_word
# 判断prefix是否存在
def starteith(self,word):
    node=self.root
    for char in word:
        node = node.data.get(char)
        if not node:
            return False
    return True
tire=Tire()
tire.insert('hollow')
print(tire.root.data)