def insertion_sort(l):
    """This function sorts the list b using insertion sort algorithm"""
    for i in range(1,len(l)):
        current_val=l[i]
        j=i-1
        while j>=0 and current_val<l[j]:
            l[j+1]=l[j]
            j=j-1
        else:l[j+1]=current_val

if __name__=="__main__":  
   l=[3,1,2,9,4,8,88,23,55,678,94939,5,6,7]

   insertion_sort(l)

   print(l)

   
   