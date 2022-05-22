"""
빌딩의 시야각이 접하지 않아야 보이는거
=> 기울기를 판단하여 가능한지 안한지 확인한다.
=> 풀이가 잘 생각이 안났는데 알고리즘 분류 보고 풀었다.
=> 50이 최댓값이기 때문에 O(n^2)로 풀리는거 같다.
"""
N = int(input())
S = [0 for i in range(N)]
B = list(map(int, input().split()))

for i in range(N):
    maxDegree = -1000000000
    y = B[i]
    x = i
    for j in range(i+1, N):
        ty = B[j]
        tx = j

        if maxDegree < (ty-y)/(tx-x):
            maxDegree = (ty-y)/(tx-x)
            S[i] += 1
            S[j] += 1
print(max(S))
