"""
MST : 그래프를 최소의 비용으로 연결하는 최적의 해답
1. 크루스칼
    정렬후에 유니온 파인드를 이용하여 사이클이 생기지 않도록 연결하는 방법
2. 프림
"""


def find(parent, node):  # 루트 노드를 찾아준다.
    if parent[node] == node:  # 자신의 값을 가지면 지가 루트임
        return node
    parent[node] = find(parent, parent[node])  # 부모노드를 기준으로 모든 노드의 부모를 루트로 바꾼다.
    return parent[node]


def union(parent, a, b):  # 두 노드를 합친다.

    a = find(parent, a)  # 루트 노드를 알아온다.
    b = find(parent, b)

    if a == b:  # 같은 그룹인지 검증
        return False

    if a <= b:
        parent[b] = a  # 루트 노드의 부모에 새로운 루트 노드로 갱신
    else:
        parent[a] = b  # 루트 노드의 부모에 새로운 루트 노드로 갱신
    return True


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: (x[2]))

    parent = [i for i in range(n)]
    for info in costs:
        A, B, C = info
        if union(parent, A, B):  # 다른 부모라면 ㄱㅊ
            answer += C
    return answer
