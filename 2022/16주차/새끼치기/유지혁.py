'''
17291
새끼치기
홀수에 태어남: 3번 분열 후 사망
짝수에 태어남 : 4번 분열 후 사망
i번째 해에 존재하는 벌레 수 = (i-1)번째에 존재하는 벌레 수 * 2 - (짝수인경우, i-3,i-4번째에 태어난 벌레 수)
'''

import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N = int(input())
	create_bugs = [0] * 21 # i번째 해에 태어난 벌레 수 
	all_bugs = [0] * 21  # i번째 해에 존재하는 벌레 수 
	all_bugs[1] = 1
	all_bugs[2] = 2
	all_bugs[3] = 4
	all_bugs[4] = 7
	create_bugs[1] = 1
	create_bugs[2] = 1
	create_bugs[3] = 2
	create_bugs[4] = 4
	
	for i in range(5, N + 1):
		#i번째 해에 태어난 벌레 수 
		create_bugs[i] = all_bugs[i - 1]
		
		#i번째 해에 존재하는 벌레 수
		if i % 2 == 0:
			all_bugs[i] = all_bugs[i - 1] * 2 - create_bugs[i - 3] - create_bugs[i - 4]
		else:
			all_bugs[i] = all_bugs[i - 1] * 2 
			
	print(all_bugs[N])
