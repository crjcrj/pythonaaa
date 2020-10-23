class Heap:
    def __init__(self):
        self.data_list=[]
    # 返回父节点的下表
    def get_parent_index(self,index):
        if index==0 or index>len(self.data_list)-1:
            return 0
        else:
            return (index-1)>>1
    # 交换
    def swap(self,index_a,index_b):
        self.data_list[index_a],self.data_list[index_b]=self.data_list[index_b],self.data_list[index_a]
    # 添加节点
    def insert(self,data):
        self.data_list.append(data)
        index=len(self.data_list)-1
        parent=self.get_parent_index(index)
        while self.data_list[parent]<self.data_list[index] and parent>=0 :
            self.swap(parent,index)
            index=parent
            parent=self.get_parent_index(index)
    # 删除节点
    def remove(self):
        remove_data=self.data_list[0]
        self.data_list[0]=self.data_list[-1]
        del self.data_list[-1]
        self.heapfy(0)
        return remove_data


    def heapfy(self,index):
        max_data_index=index
        total_index=len(self.data_list)-1
        while True:
            if 2*index+1<=total_index and self.data_list[2*index+1]>self.data_list[max_data_index]:
                max_data_index=2*index-1
            if 2*index+2<=total_index and self.data_list[2*index+1]>self.data_list[max_data_index]:
                max_data_index=2*index-1
            if max_data_index==index:
                break
            self.swap(max_data_index,index)
            index=max_data_index

if __name__ == '__main__':
    ll=Heap()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)

    print(ll.data_list)