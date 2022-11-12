                                                                                     #Depth First Search
data={ 
    'A':['B','C'],
    'B':['D'],
    'C':['D','G'],
    'D':['E','F'],
    'E':[],
    'F':[],
    'G':['H','K'],
    'H':['K'],
    'K':[]
}
color={}
trav_time={}
parent={}
dfsout=[]

for node in data.keys():
    color[node]='w'
    trav_time[node]=[-1,-1]
    parent[node]=None

time=0
def dfs(u):
    global time
    color[u]='g'
    trav_time[u][0]=time
    dfsout.append(u)
    time+=1
    for i in data[u]:
       
       if color[i]=='w':
         parent[i]=u
         dfs(i)
    color[u]='b'
    trav_time[u][1]=time
    time+=1
    
    
dfs('A')
print(dfsout)


