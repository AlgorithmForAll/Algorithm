'''
문제 :idx번째 노드 & idx노드의 자식노드를 삭제한 후에 리프노드의 개수 출력
알고리즘 :DFS
풀이 방법 : idx번째 노드와 해당 idx번째 노드를 부모 노드로 하는 노드를 재귀로 찾아 삭제 후, 트리를 순회하면서
 노드 별 부모로 호출된 횟수를 저장(tree[i] = -2면 해당 노드는 삭제된 노드이므로 parent_count[-2] = -2로 함)
헷갈렸던 것 : 첨에 -2인 경우 parent_count[i] = -2로 안하니까 해당 노드들까지 리프 노드로 판정됨
'''
import sys
input = sys.stdin.readline
tree = list()
N = 0

def delete(idx):
	global tree
	#idx번째 노드 삭제 (부모 노드를 -2로 부여)
	tree[idx] = -2
	
	#idx의 자식 노드 삭제
	for j in range(N):
		if tree[j] == idx:
			delete(j)	
	
if __name__ == "__main__":
	N = int(input())
	tree = list(map(int,input().split()))
	idx = int(input())
	answer = 0

	#idx번 노드 및 자식 노드 삭제 
	delete(idx)
	
	#리프 노드 탐색 시작 : 0~N-1번 중 부모 노드로 호출되지 않은 대상 탐색 
	parent_count = [0] * N
	for i in range(N):
		parent = tree[i]
		if parent == -2: #삭제된 노드인 경우, 자신의 count값을 -2로 함 
			parent_count[i] = -2
		elif parent >= 0:
			parent_count[parent] += 1
	
	answer = parent_count.count(0)
	print(answer)
	

