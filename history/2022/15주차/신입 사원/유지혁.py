'''
1946 신입사원 
문제 : 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발할 때( 
즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않음)
선발할 수 있는 신입사원의 최대 인원수
알고리즘 : 그리디
힌트 : 동등 석차는 없다 -> 정렬이 가능하다 // 등수끼리 비교 : sort(), 그리디
풀이 : 1차 서류 등수 기준으로 정렬 후(1등이 가장 앞에 존재), for문 돌면서 지금까지의 최대 등수(가장 낮은 값)보다도 좋은 등수를 받았다면,
해당 지원자는 신입사원으로 들 수 있다.
'''

import sys
input = sys.stdin.readline

if __name__ == "__main__":
	T = int(input())
	while T:
		N = int(input())
		arr = list(list(map(int,input().split())) for _ in range(N))
		answer = 0 #최대 선발인원 수 
		#1. 1차 시험 등수 기준으로 정렬
		arr.sort(key = lambda x : x[0])
		
		# 2. 탐색하면서 최대 지원자 수 구하기 
        #  : i번째 지원자가 이전 지원자들(자신보다 1차 등수가 높은 지원자)의 최대 등수(최소 값)보다 
        # 등수가 높다면 i번째 지원자는 선발 가능
		cnt = 0
		_min = N + 1 
		for i in range(len(arr)):
			apply = arr[i]
            # 선발 가능 
			if apply[1] < _min:
				cnt += 1
				_min = apply[1]

		answer = cnt
		print(answer)
		T -= 1

