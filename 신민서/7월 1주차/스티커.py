#난 분명히 제대로 한 것 같은데 99프로에서 실패ㅠㅠㅠㅠㅠㅠㅠ

t = int(input())
for tt in range(t):
    arr = []
    l = int(input())
    D = [[0 for _ in range(l)] for __ in range(2)]
    for i in range(2):
        arr.append(list(map(int, input().split())))
    D[0][0] = arr[0][0]
    D[1][0] = arr[1][0]
    if l == 1:
        print(max(arr[0][0], arr[1][0]))
        exit(0)
    D[0][1] = D[1][0] + arr[0][1]
    D[1][1] = D[0][0] + arr[1][1]
    for i in range(2, l):
        D[0][i] = max(D[1][i-1] + arr[0][i], D[1][i-2] + arr[0][i])
        D[1][i] = max(D[0][i-1] + arr[1][i], D[0][i-2] + arr[1][i])
    print(max(D[0][l-1], D[1][l-1]))