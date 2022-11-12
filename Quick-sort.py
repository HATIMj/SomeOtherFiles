def swap(l,a,b):
    l[a],l[b]=l[b],l[a]
    

def partition(l,start,end):
    
    pivot_index=start
    pivot=l[pivot_index]

    while start<end:
        while start<len(l) and l[start]<=pivot:
            start+=1
        while l[end]>pivot:
            end-=1

        if start<end:
            swap(l,start,end)
    swap(l,pivot_index,end)
    return end
    

def quick_sort(l,start,end):
    if start<end:
       pi=partition(l,start,end)

       quick_sort(l,start,pi-1)
       quick_sort(l,pi+1,end)
if __name__=="__main__":  
   l=[3,1,2,4,5,6,7]
   quick_sort(l,0,len(l)-1)
   print(l)

   