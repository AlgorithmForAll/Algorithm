'''
2250 트리의 높이와 너비 
'''
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)] #tree[i] : i번째 노드의 왼쪽자식/오른쪽자식을 저장한 리스트 
left_min = [ N for _ in range(N + 1)]  # left_min[i] : i level에 있는 node 중 가장 왼쪽에 있는 node 의 위치
right_max = [ 0 for _ in range(N + 1)] # right_max[i] : i level에 있는 node 중 가장 오른쪽에 있는 node 의 위치
order = 1 #탐색 순서(열) 

# arguments    : 현재 node 번호, 탐색 순서(열), level
# function     : 레벨 별 max_width를 탐색하는 함수(중위순회로 탐색) 
def update_max_width(cur_node, level):
    global N, tree, left_min, right_max, order 
    #왼쪽 서브 노드가 있는 경우, 왼쪽 탐색 
    if tree[cur_node][0] > 0:
        update_max_width(tree[cur_node][0], level + 1)

    #현재 노드 visit(현재 노드가 속한 레벨의 가장 왼쪽 값, 가장 오른쪽 값 update)
    #order : 현재 노드의 탐색 순서(열 값)
    left_min[level] = min(left_min[level], order)
    right_max[level] = max(right_max[level], order)
    order += 1
    
    #오른쪽 서브 노드가 있는 경우, 오른쪽 탐색  
    if tree[cur_node][1] > 0:
        update_max_width(tree[cur_node][1], level + 1)
    
if __name__ == "__main__":
    # 0. input받기 
    for i in range(N):
        cur_node, left_node, right_node = map(int, input().split())
        tree[cur_node] = [left_node, right_node]
    
    # 1. root node 구하기
    #is_root[i] : i번 노드가 root노드이면 True, 아니면 False
    root = 0
    is_root = [ True for _ in range(N + 1) ]
    is_root[0] = False
    for i in range(1, N + 1):
        if tree[i][0] > 0:
            is_root[tree[i][0]] = False
        if tree[i][1] > 0:
            is_root[tree[i][1]] = False
    root = is_root.index(True)
   
    # 2. 중위 순회하며 level 별 min, max 값 업데이트
    update_max_width(root, 1)

    # 3. level 별 min, max를 통해 width 저장
    max_width_list = [ (right_max[i] - left_min[i] + 1) for i in range(N + 1) ]
    
    # 4.max_width, max_level 출력 
    max_width = max(max_width_list)
    max_level = max_width_list.index(max_width)
    print(max_level, max_width)
