"""
1. 조합으로 숫자 만들기
2. 차가 가장 최소가 되게 하는 값
3. 숫자 개수와 차를 더하기

1. 100 기준으로 차가 몇인지도 포함하기

pypy3으로 제출....ㅠㅠ

python으로 제출하려면 한자리씩 확인해야한다.
DFS로 풀면 안됨.
"""
N = int(input())
M = int(input())
Ms = []
if M != 0:
    Ms = list(map(int, input().split()))

btn = []
for i in range(10):
    if i not in Ms:
        btn.append(str(i))

btns = []

small = 999999999999


def DFS(ch):
    global btn
    global small
    if len(ch) > len(str(N))+1:
        return
    # 여기서 검사
    if len(ch) >= len(str(N))-1:
        channel = int(ch)
        small = min(small, abs(N-channel) + len(str(channel)))

    for i in btn:
        DFS(ch+i)


for i in btn:
    DFS(i)

small = min(small, abs(N-100))
print(small)
