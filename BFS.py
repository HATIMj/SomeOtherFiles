                                                                                   #Breadth First Search




data={
    'A':['B','C'],
    'B':['D'],
    'C':['G'],
    'D':[],
    'G':[]
    
}
level={}
parent={}
visited={}
bfsout=[]
for node in data.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
j=[]
def bfs(u):
    visited[u]=True
    level[u]=0
    j.append(u)
    while not len(j)==0:
        k=j.pop(0)
        bfsout.append(k)
        for i in data[k]:
            if not visited[i]:
               
               parent[i]=k
               level[i]=level[k]+1
               j.append(i)
    
print(bfs('A'))
v='G'
path=[]
while v is not None:
    path.append(v)
    parent[v]=v
    print(path)
print(bfsout)





