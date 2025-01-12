def checkPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True
            
num = 5
print(checkPrime(num))