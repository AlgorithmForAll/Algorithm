import sys
input = sys.stdin.readline

def solve(i, j):
    if j == C-1:
        return True
    for k in dx:
        if 0 <= i+k < R and arr[i+k][j+1] == '.' and not visited[i+k][j+1]:
            visited[i+k][j+1] = True
            
            if solve(i+k, j+1):
                return True
    return False

R, C = map(int, input().split())
arr = [list(input().strip()) for i in range(R)]
visited = [[False]*C for i in range(R)]

dx = [-1, 0, 1]
result = 0

for i in range(R):
    if arr[i][0] == '.':
        if solve(i, 0):
            result += 1
            
print(result)    