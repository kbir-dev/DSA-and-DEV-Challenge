def sort(arr):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
    
arr = [6,4,3,8,2,7,4,1,9,12]
n = len(arr)
print("Array before sorting :",arr)
arr = sort(arr)
print("Array after sorting :",arr)