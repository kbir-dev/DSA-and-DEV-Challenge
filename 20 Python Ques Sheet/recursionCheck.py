def factorialCalculation(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * factorialCalculation(num-1)
    
num = 5
print(factorialCalculation(num))