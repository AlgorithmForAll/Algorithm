'''
11660
구간합구하기5
(x1,y1)을 왼쪽 상단 꼭짓점, (x2,y2)를 오른쪽 하단 꼭짓점으로 하는 직사각형 범위의 합
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N, M = map(int,input().split())
	# arr의 index를 맞추기 위해 맨 위 / 맨 왼쪽에 배열 삽입
	arr = [[0] * (N + 1)]
	for _ in range(N):
		tmp = [0]
		tmp.extend(list(map(int,input().split())))
		arr.append(tmp)

	#dp[i][j] = (1,1)에서 (i,j)까지 직사각형범위에 있는 수들의 합
	dp = list([0] * (N + 1) for _ in range(N + 1))
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			dp[i][j] = arr[i][j] + (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1])

	# M개의 테스트 케이스
	for _ in range(M):
		x1, y1, x2, y2 = map(int,input().split())
		#x1,y1에 1씩 빼야 함 
		x1 -= 1
		y1 -= 1
		print(dp[x2][y2] - dp[x1][y2] - dp[x2][y1] + dp[x1][y1])
