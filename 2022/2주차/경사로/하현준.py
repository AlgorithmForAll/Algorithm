"""
경사로
https://www.acmicpc.net/problem/14890
"""
N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def validate(road):
    check = True
    count = [0 for _ in range(N)]
    count[0] = 1
    for j in range(1, N):
        if road[j] == road[j - 1]:
            count[j] = count[j - 1] + 1
        else:
            count[j] = 1

    for j in range(1, N):
        if abs(road[j] - road[j - 1]) > 1:
            check = False
            break
        elif road[j] - road[j - 1] == 1:
            if count[j - 1] < L:
                check = False
                break
        elif road[j] - road[j - 1] == -1:
            if not (j + L - 1 < N and road[j + L - 1] == road[j] and count[j + L - 1] >= L):
                check = False
                break
            else:
                for k in range(j, j + L):
                    count[k] = -1
                now = j + L
                while now < N and road[now] == road[j]:
                    count[now] -= L
                    now += 1

    return 1 if check else 0


for i in range(N):
    answer += validate(graph[i])

graph = list(map(list, zip(*graph)))

for i in range(N):
    answer += validate(graph[i])
print(answer)
