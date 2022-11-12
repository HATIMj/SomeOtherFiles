class Accounts:
    def __init__(self,dict):
        self.dict=dict
    def balance_sheet(self):
        f=open("balance.txt",'w')
        a={}
        l={}
        m=0
        assets=['land','building','cash','bank','machinary','debtor']
        liability=['capital','bills payable','creditors','bank-loans']
        n=0
       
       
        for i,j in self.dict.items():

            if i=='dep':
                l=int(a['machinary'])-int(j)
                a['machinary']=l
                
                

            elif i=='prov':
                k=int(a['debtor'])-int(j)
                a['debtor']=k
                
            
            
            if i in assets :
                
                a[i]=j
                m+=int(j)
            elif i in liability:
                l[i]=j
                n+=int(j)
        print(a)
        a['total']=m
        l['total']=n
        f.write("Assets\n")
        f.write(f"--------\n")

        for i,j in a.items():
            f.write(f"{i}|{j}\n")
        f.write(f"--------\n")
        f.write("Liabilities\n")
        f.write(f"--------\n")
        for i,j in l.items():
            f.write(f"{i}|{j}\n")
        f.write(f"--------")
        if a['total']==l['total']:
           print("balance sheet matched succesfully")
        else:
            print("balance sheet did not matched successfully")
        f.close()         
if __name__=="__main__":
    dict={}
    while True:
        i=input("write the item and its value separated by space.").split(" ")
        if i[0]=="stop":
           break
        else:dict[i[0]]=i[1]
    x=Accounts(dict)
    x.balance_sheet()
    