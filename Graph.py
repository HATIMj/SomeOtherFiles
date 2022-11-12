                                                                              #GRAPH DATA STRUCTURE IN PYTHON
        for start,end in edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start]=[end]
        print(self.dict)        

    def get_path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.dict:
            return []
        paths=[]
        for n in self.dict[start]:
            if n not in path:
                new_path=self.get_path(n, end,path)
            for i in new_path:
                paths.append(i)
        return paths

    def shortpath(self,start,end,path=[]):

        path=path+[start]
        if start==end:
            return [path]
        if start not in self.dict:
            return []
        paths=[]
        dtp=None
        for n in self.dict[start]:
            if n not in path:
                sp=self.shortpath(n,end,path)
            if sp:
                if dtp is None or len(sp) < len(dtp):
                    dtp=sp
        return dtp

l=[("jojo","lojo")
   ,("lojo","uiop")
   ,("jojo","ufhs")]
j=Graph(l)
print(j.shortpath("jojo","uiop"))
