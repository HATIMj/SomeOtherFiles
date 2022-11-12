def fnj(j):
    l={}
    for k in j:
        i=k
        m=0
        for x in j:
            if i==x:
                m+=1
                l[x]=m
    for i,j in l.items():
        if j==1:
            print(i)
            break

  

if __name__=="__main__":
    j=input().lower()

    fnj(j)