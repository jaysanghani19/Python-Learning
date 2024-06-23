def sort(arr):
    size = len(arr)

    for i in range (0 , size-1):
        for j in range (0,size-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            
arr = [2,5,3,1,9,12]
sort(arr)
print(arr)