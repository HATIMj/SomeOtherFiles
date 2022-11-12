class Tree:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        l=0
        p=self.parent
        while p:
            l+=1
            p=p.parent
        return l
    def print_tree(self):
        s=' '*self.get_level() *3
        pre=s+'|--'
        print(pre+self.data)
        if self.children:
           for child in self.children:
               child.print_tree()
def build_tree():
    root=Tree("0")
    j=Tree("1")
    k=Tree("2")
    j.add_child(Tree("3"))
    j.add_child(Tree("4"))

    k.add_child(Tree("5"))
    k.add_child(Tree("6"))
    
    root.add_child(j)
    root.add_child(k)
    root.print_tree()











if __name__=="__main__":
    build_tree()
