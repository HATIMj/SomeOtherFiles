class Library:
    def __init__(self,list,name):
       self.list=list
       self.name=name
    def show(self):
        for i in self.list:
            print(i)
    def add(self,abook):
        self.book=abook

        for i in range(1):
            self.list.append(self.book)
        
    def lend(self,lbook):
        self.book=lbook
        for i in self.list:
            if i==self.book:
                v.append(i)
                self.list.remove(i)
                c.append(self.name)
    def returnb(self,lbook):
        self.book=lbook
        for i in v:
            if i==self.book:
                v.remove(i)
                self.list.append(i)
            else:
                print("no one have lended this book.")

    def show_dict(self):
        u=v
        q=c
        pass











v=[]
c=[]
d={}
if __name__=='__main__':
    s=list(map(str,input("Books name separated by space:--").split(" ")))
    
