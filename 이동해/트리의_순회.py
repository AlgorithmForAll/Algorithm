import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0] * (n + 1)
# 인오더 값의 인덱스 정보 입력
for i in range(n):
    pos[in_order[i]] = i

def pre_order(istart, iend, pstart, pend):
    if istart > iend or pstart > pend:
        return

    # 루트 노드는 포스트오더의 마지막 값
    root = post_order[pend]

    # 루트를 기준으로 왼쪽, 오른쪽 개수 세기
    left_cnt = pos[root] - istart
    right_cnt = iend - pos[root]

    # 프리오더: 루트 - 왼쪽 서브트리 - 오른쪽 서브트리
    print(root, end=' ')

    # 왼쪽 서브트리
    pre_order(istart, pos[root]-1, pstart, pstart+left_cnt-1)
    # 오른쪽 서브트리
    pre_order(pos[root]+1, iend, pend-right_cnt, pend-1)


pre_order(0, n-1, 0, n-1)