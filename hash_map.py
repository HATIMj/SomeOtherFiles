                                                                         #HASHMAP --Completely working , Also Handles collision handling


class Hash:
    def __init__(self):
        self.Max=10
        self.ar=[[] for i in range(self.Max)]
    def get_Hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.Max

    def __getitem__(self,key):
        index=self.get_Hash(key)
        for i in self.ar[index]:
            if i[0]==key:
                print(i[1])
    def __setitem__(self,key,val):
        index=self.get_Hash(key)
        found=False
        for i,ele in enumerate(self.ar[index]):
            if len(ele)==0 and ele[0]==key: 
                self.ar[index][i]=(key,val)

                found=True
               
            
        if not found:
            self.ar[index].append((key,val))


    def __delitem__(self,key):
        index=self.get_Hash(key)
        for id,i in enumerate(self.ar[index]):
            if i[0]==key:
                del self.ar[index][id]




if __name__=="__main__":
    j=Hash()
    j['mar']=99
    j['mar']
    j['march 6']=78
    j['march 17']=987
    j['march 17']=777
    del j['march 17']
    del j['march 17']
    print(j.ar)
    del j['mar']
    print(j.ar)