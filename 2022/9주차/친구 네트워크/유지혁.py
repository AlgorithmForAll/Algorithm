'''
4195 친구 네트워크 
사이트의 친구관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구네트워크에 몇 명이 있는지 구하라 
알고리즘 : union find(disjoint-set) / 다른 노드들 중에 연결된 노드를 찾거나 노드를 합칠 때 사용 

'''
import sys
input = sys.stdin.readline


def find(parent,a):
	if parent[a] == a:
		return a
	
	parent[a] = find(parent,parent[a])
	return parent[a]

def union(parent,cnt,a,b):
	roota = find(parent,a)
	rootb = find(parent,b)

	if roota < rootb:
		parent[rootb] = roota
		cnt[roota] += cnt[rootb]
		
	elif rootb < roota:
		parent[roota] = rootb
		cnt[rootb] += cnt[roota]

if __name__ == "__main__":
	T = int(input())
	while T:
		F = int(input())
		parent = {} 
		cnt = {} #친구 네트워크 명수. root의 친구 네트워크 명 수 = 해당 그룹의 친구 네트워크 명 수  

		for _ in range(F):
			a,b = input().split()
			if a not in parent:
				parent[a] = a
				cnt[a] = 1

			if b not in parent:
				parent[b] = b
				cnt[b] = 1
			
			union(parent,cnt,a,b)
			print(max(cnt[parent[a]],cnt[parent[b]]))

		T -= 1
