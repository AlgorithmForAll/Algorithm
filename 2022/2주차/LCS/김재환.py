A = list(input())
B = list(input())
tmp = [[0 for i in range(len(A)+1)] for i in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if B[i-1] == A[j-1]:
            tmp[i][j] = 1
for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if tmp[i][j] == 1:
            tmp[i][j] = tmp[i-1][j-1]+1
        else:
            tmp[i][j] = max(tmp[i-1][j], tmp[i][j-1])

print(tmp[-1][-1])
# 따로 정리해 보는 시간이 필요할듯
