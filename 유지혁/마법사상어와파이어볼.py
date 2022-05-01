import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    fireballs = []
    arr = [[[] for _ in range(N)] for _ in range(N)]
    dir = [[-1, 0], [-1,1], [0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    for _ in range(M):
    	x, y, m, s, d = list(map(int, input().split()))
    	fireballs.append([x-1, y-1, m, s, d])

    #파이어볼 이동
    for _ in range(K):
        while fireballs:
        	cx, cy, cm, cs, cd = fireballs.pop()
        	nx = (cx + cs * dir[cd][0]) % N  
        	ny = (cy + cs * dir[cd][1]) % N
        	arr[nx][ny].append([cm, cs, cd])


        for x in range(N):
            for y in range(N):
                #2개 이상인 경우 
                if len(arr[x][y]) > 1:
                    sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(arr[x][y])
                    while arr[x][y]:
                        m, s, d = arr[x][y].pop()
                        sum_m += m
                        sum_s += s
                        if d % 2:
                            cnt_odd += 1
                        else:
                            cnt_even += 1
                    if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]
                    if sum_m//5:  # 소멸
                        for d in nd:
                            fireballs.append([x, y, sum_m//5, sum_s//cnt, d])

                # 1개인 경우
                if len(arr[x][y]) == 1:
                    fireballs.append([x, y] + arr[x][y].pop())

    print(sum([f[2] for f in fireballs]))
