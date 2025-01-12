import math
arr = [5,4,2,7,9,1,5,89,4,3,78,32,677,321,574,964,322]
min = math.inf
max = -math.inf
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]
print("max :",max," min :",min )