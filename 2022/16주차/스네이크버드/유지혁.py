import sys
input = sys.stdin.readline
import heapq

if __name__ == "__main__":
	N,snake = map(int,input().split())
	apples = list(map(int,input().split()))
	heapq.heapify(apples)
	
	#스네이크버드의 최대길이
	while apples:
		apple = heapq.heappop(apples)
		if snake < apple:
			break
		snake += 1
	
	print(snake)
