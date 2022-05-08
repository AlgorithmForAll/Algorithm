from itertools import permutations
import copy
import sys
input = sys.stdin.readline
MAX = 5001


def rotate(a, i):
    r, c, s = i[0]-1, i[1]-1, i[2]
    
    # 돌리기
    while s:
        query = r-s, r+s, c-s, c+s
        
        right, left, up, down = query
        
        # 전 값을 빼놓아야 값이 오버라이딩 되는 것을 막음
        temp = a[right][up]
        # up
        for i in range(right, left):
            a[i][up] = a[i+1][up]
        # left
        for i in range(up, down):
            a[left][i] = a[left][i+1]
        # down
        for i in range(left, right, -1):
            a[i][down] = a[i-1][down]
        # right
        for i in range(down, up, -1):
            a[right][i] = a[right][i-1]
        
        a[right][up+1] = temp     
        
        s -= 1
    return a
        
N, M, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
turn = []
for i in range(K):
    turn.append(list(map(int, input().split())))

# 순서를 조합으로 꺼내서 경우의 수 계산 turn C K 
check = list(permutations(turn, K))

# 조합의 경우의 수 만큼 돌리기
for i in check:
    # 경우의 수 마다 초기 배열에서 회전을 해야하기 때문에 카피 필요
    a = copy.deepcopy(arr)
    for j in i:
        after = rotate(a, j)
    
    # 경우의 수 마다 행별 최소값 체크
    sum_m = 5001
    for i in range(N):
        sum_m = min(sum(after[i]), sum_m)
    
    MAX = min(MAX, sum_m)

print(MAX)