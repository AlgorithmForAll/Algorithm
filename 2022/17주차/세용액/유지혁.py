'''
알고리즘 : 투포인터
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	arr = list(map(int,input().split()))
	arr.sort()
	min_val = sys.maxsize
	answer = list()
	for i in range(N - 2):
		st = i + 1
		ed = N - 1
		while st < ed:
			tmp_sum = arr[i] + arr[st] + arr[ed]
			if abs(tmp_sum) < min_val:
				min_val = abs(tmp_sum)
				answer = [arr[i], arr[st], arr[ed]]
				
			if tmp_sum < 0:
				st += 1
			elif tmp_sum > 0:
				ed -= 1
			else:
				break

	for i in range(3):
		print(answer[i], end=' ')
