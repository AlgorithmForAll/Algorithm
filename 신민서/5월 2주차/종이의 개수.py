def division(r, c, size):
    global minus, zero, one
    flag = 1
    num = arr[r][c]
    for i in range(r, r+size):
        for j in range(c, c+size):
            if arr[i][j] != num:
                flag = 0
    if flag == 1:
        if num == 0:
            zero += 1
        elif num == 1:
            one += 1
        elif num == -1:
            minus += 1
    else:
        size //= 3
        division(r, c, size)
        division(r+size, c, size)
        division(r+size*2, c, size)
        division(r, c+size, size)
        division(r, c+size*2, size)
        division(r+size, c+size, size)
        division(r+size*2, c+size, size)
        division(r+size, c+size*2, size)
        division(r+size*2, c+size*2, size)


n = int(input())
arr = [list(map(int, input().split())) for __ in range(n)]

minus = 0
zero = 0
one = 0

division(0, 0, n)
print(minus)
print(zero)
print(one)