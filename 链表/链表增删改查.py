class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)
class linklist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
        curr=self.head
        for _ in range(1,index):
            curr=curr.next
        return curr


    # 输出
    def __repr__(self):
        curr=self.head
        str_repr=""
        while curr:
            str_repr+="{} -->".format(curr)
            curr=curr.next
        return str_repr + "end"

    def insert(self,index,data):
        new_data=Node(data)
        if index<0 or index>self.size :
            return "cowu"
        else:
            if self.size==0:
                self.head=new_data
                self.tail=new_data
            elif  index==0:
                new_data.next=self.head
                self.head=new_data
            elif index==self.size:
                self.tail.next=new_data
                self.tail=new_data
            else:
                prev=self.get(index-1)
                new_data.next=prev.next
                prev.next=new_data
            self.size+=1
    # 删除结点
    def select(self,index):
        if index<0 or index>=self.size:
            return "cuowu"
        if index==0:
            remove_node=self.head
            self.head=self.head.next
            remove_node=None
        elif index==self.size-1:
            prve=self.get(index-1)

            prve.next=None
            self.tail=prve
        else:
            prve=self.get(index-1)
            prve.next=prve.next.next
        self.size -=1
    # 翻转
    def reserve(self):
        prve=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prve
            prve=curr
            curr=next_node
        self.head=prve

ll=linklist()
ll.insert(0,1)
ll.insert(1,2)
ll.insert(2,3)
ll.insert(2,3)
print(ll)


