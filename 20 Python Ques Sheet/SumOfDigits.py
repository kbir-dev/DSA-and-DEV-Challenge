def sumOfDigits(num):
    sum = 0
    while num != 0:
        last = num%10
        sum+=last
        num=num//10
    return sum
    
n = 19234
print(sumOfDigits(n))