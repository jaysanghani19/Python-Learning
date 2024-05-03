def bs_regular(arr,target):
    low =0
    high = len(arr)-1

    while low <= high:
        mid = low + (high-low)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    
    return -1

def bs_recursion(arr,target,low,high):
    
    if low <= high:
        mid = low + (high-low)//2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            return bs_recursion(arr,target,mid+1,high)
        else:
            return bs_recursion(arr,target,low,mid-1)
        
    return -1
        

     
arr = [1,5,8,10,15,25]

# print(arr[bs_regular(arr,8)])
# print(bs_regular(arr,25))

print(bs_recursion(arr,1,0,(len(arr)-1)))
print(bs_recursion(arr,25,0,(len(arr)-1)))