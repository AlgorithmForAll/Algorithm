"""
10
1 2 3 4 5 6 7 8 9 10
"""
import sys
input = sys.stdin.readline

N = int(input())
target = list(map(int, input().split()))
target.sort()

count = 0
for i in range(N):
    tmp = target[:i] + target[i+1:]  # i번째 값을 제외한 리스트를 만든다.
    L, R = 0, len(tmp)-1
    # N이 2000이하 이기 때문에 투포인터로 검증하는 경우 2000*2000으로 4,000,000 시간 복잡도 안에 계산이 완료된다.
    while L < R:
        t = tmp[L] + tmp[R]
        if t == target[i]:  # 새롭게 만든 리스트에서 투포인터로 합이 target[i]가 되는지 검증한다.
            count += 1
            break
        elif t > target[i]:
            R -= 1
        else:
            L += 1
print(count)
