"""
유니온파인드 참고: https://0x15.tistory.com/34
"""
# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
parent = [0] * (n + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(n-2):
    a, b = map(int, input().split())
    union(a, b)

# 각 원소가 속한 집합 출력하기
for i in range(2, n + 1):
    if find(i) != 1:
        print(1, i)
        break