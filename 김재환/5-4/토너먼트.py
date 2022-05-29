"""
16 1 2
걍 무식하게 풀되, A,B의 값을 계속 가져가기
"""
N, A, B = map(int, input().split())
tmp = [i for i in range(1, N + 1)]


def calc(tmp):
    global A
    global B
    round = 0
    while True:
        n = len(tmp) // 2
        round += 1
        for ni in range(n):
            i = 2*ni
            if tmp[i] == A and tmp[i+1] == B:
                return round
            if tmp[i] == B and tmp[i+1] == A:
                return round

            if tmp[i] == A or tmp[i+1] == A:
                A = ni+1
            if tmp[i] == B or tmp[i+1] == B:
                B = ni+1
        tmp = [i for i in range(1, len(tmp)//2+2)]
        if B > len(tmp):
            B = tmp[-1]
        if A > len(tmp):
            A = tmp[-1]


print(calc(tmp))
