def binarySearch(arr,target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1
        
        

arr = [1,2,3,45,67,123,543,1234]
index = binarySearch(arr,122)
if index == -1:
    print("Target doesnt exist in array")
else:
    print("Target exists in array")
