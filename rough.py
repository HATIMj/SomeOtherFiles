nums=[8, 7, 2, 5, 3, 1]
def finddiff(nums,diff):
    s=set()
    i=0
    while i<len(nums):
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        if nums[i]-diff in s:
            print(nums[i],nums[i]-diff)
        if nums[i]+diff in s:
            print(nums[i],nums[i]+diff)
        s.add(nums[i])
        i+=1
finddiff(nums, 3)