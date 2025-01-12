def checkArmstrong(num):
    origin_num = num
    sum = 0
    while num != 0:
        last = num%10
        cube = last*last*last
        sum += cube
        num = num//10
    if sum == origin_num:
        return True
    else:
        return False
    
num = 122
print(checkArmstrong(num))