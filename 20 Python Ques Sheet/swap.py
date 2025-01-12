def swap(x,y):
    x = x + y
    y = x - y
    x = x - y
    return x , y
    
x = 2
y = 5
print("Before Swapping: "+str(x)+" "+str(y))
x , y = swap(x,y)
print("After Swapping : "+str(x)+" "+str(y))