class Binary_Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def add_child(self,data):
        if data==self.data:
            return 
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_Tree(data) 
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_Tree(data)
    def search(self,val):
        if val==self.data:return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.max()
    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            min_val=self.left.min()
            self.data=min_val
            self.right=self.right.delete(min_val)
            
            return self
    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
def build_tree(l):
    root=Binary_Tree(l[0])
    for i in range(1,len(l)):
        root.add_child(l[i])
    return root
if __name__=="__main__":
    l=[30,10,20,2,4,5,22,33,5,44,66,24]
    m= build_tree(l)
    print(m.in_order_traversal())
    print(m.delete(44))
    print(m.in_order_traversal())