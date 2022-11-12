def bubble(l):
    for i in range(len(l)):
        swapped=False
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                tmp=l[j]
                l[j]=l[j+1]
                l[j+1]=tmp
                swapped=True
        if not swapped:
            break
    return l
print(bubble([2,66,3,27,43]))