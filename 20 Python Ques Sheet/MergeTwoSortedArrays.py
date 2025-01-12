arr1 = [1,2,3,4,5]
arr2 = [2,5,6,8,10]
a1 = 0
a2 = 0
arr3 = list() 
while a1 < len(arr1) and a2 < len(arr2):
    if arr1[a1] <= arr2[a2]:
        arr3.append(arr1[a1])
        a1 += 1
    else:
        arr3.append(arr2[a2])
        a2 += 1
while a1 < len(arr1):
     arr3.append(arr1[a1])
     a1 += 1
while a2 < len(arr2):
     arr3.append(arr2[a2])
     a2 += 1
print(arr3)