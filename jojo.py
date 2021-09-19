if __name__ == '__main__':
    ls=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
       
        ls.append([score,name])
    
    k=min(ls)
    c=ls.count(k)
    for k in range(c):
        ls.remove(min(ls))
    j=max(ls)
    while max(ls)==j:
        ls.remove(j)
    k=max(ls)
    while max(ls)==k:
        ls.remove(k)
    p=min(ls)
    print('\n'.join([name for score,name in ls if score==p]))
