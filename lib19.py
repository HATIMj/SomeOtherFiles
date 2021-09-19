class Library:
    def __init__(self,list,name):
        self.list=list
        self.name=name
    def add(self,abook):
        self.book=abook
        for i in range(1):
            self.list.append(self.book)
        print(self.list)
jojo=Library(['j','k','x'],'jojo')
jojo.add('y')