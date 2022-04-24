'''
알고리즘 : 정렬 
'''
import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	arr = list(list(map(int,input().split())) for _ in range(N))
	arr.sort() #시작 시간 기준 정렬 
	class_room = [arr[0][1]]

	for i in range(1,N):
		#가장 빨리 끝나는 강의실 시간보다 먼저 시작한다면 강의실 추가  
		if arr[i][0] < class_room[0]:
			heapq.heappush(class_room, arr[i][1])
	
		else:
			heapq.heappop(class_room)
			heapq.heappush(class_room, arr[i][1])

	print(len(class_room))
