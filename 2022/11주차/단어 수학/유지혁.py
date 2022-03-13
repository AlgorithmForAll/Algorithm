'''
10개의 알파벳에 각각 0~9 사이의 숫자를 대입할 때, N개의 단어가 주어질때 그 수의 합을 최대로 만들어라
알고리즘 : 그리디 
헷갈린 것 : string은 reverse가 없으므로 ''.join(reversed()) 로 할 것
			딕셔너리를 value 기준으로 정렬하는 법 : sorted(d.items(), key = lambda x : x[1]) 
앞으로 총 합을 구할 땐 이런 방식으로도 풀어볼 것 
'''
import math
import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	alpha = {} #각 알파벳이 어떤 값만큼 있는지를 저장하는 dict 
	answer = 0

	# alpha dict에 값 삽입 
	for _ in range(N):
		arr = ''.join(reversed(input().rstrip())) #한자리 수부터 입력하기 위해 reverse()
		
		for i in range(len(arr)):
			s = arr[i]
			if s not in alpha:
				alpha[s] = math.pow(10,i)
			else:
				alpha[s] += math.pow(10, i)
				
	s_alpha = sorted(alpha.items(), key = lambda x : x[1], reverse = True)

	# 가장 큰 숫자부터 내림차순 대입 후 합 구하기 
	num = 9
	for item in s_alpha:
		val = item[1]
		answer += num * val
		num -= 1

	print(int(answer))
