def sort(arr):
    size = len(arr)
    for i in range(0,size-1):
        for j in range(i,size-1):
            print(f"i : {i}  j : {j}")
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

arr = [2,5,3,1,9,12,5]
sort(arr)
print(arr)