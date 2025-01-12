a = [[1,2,3],[4,5,6],[7,8,9]]
n = len(a)
b = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        b[i][j] = a[j][i]
print(b)                 