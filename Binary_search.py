l=[1,2,3,4,5,6,7,8,9,11,22,33,44,66,77,88,99]
def bs(l,n):
   """This Function performs binary search in iteration"""
   left=0
   right=len(l)
   if left>right:
       return -1 
   while left<=right:
      midval=(left+right)//2
      mid=l[midval]
      if mid==n:
          return midval
      if mid>n:
          right=midval-1
      if mid<n:
          left=midval+1
   



def bsr(l,n,left,right):
    """This function performs binary search in recursive function"""
    
    midval=(left+right)//2
    mid=l[midval]
    if mid==n:
        return midval
    if mid>n:
        right=midval-1
    if mid<n:
        left=midval+1
    return bsr(l,n,left,right)
    
    






print(bs(l,44))
print(bsr(l,4,0,len(l)))