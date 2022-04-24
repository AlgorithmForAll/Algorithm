'''
구현 - index체크하기
'''
import sys
input = sys.stdin.readline

max_sum = 0
yuts = list()
dices = list()

def go(horses,idx,sums):
	global max_sum,yuts,dices

	if idx == 10:
		print("horses = ",horses,", sums = ",sums)	
		max_sum = max(max_sum,sums)
		return	
	
	move = dices[idx]
	for i in range(4):
		cur_hor = list(horses)
		cur_pos = cur_hor[i] #현재 위치 
		nex_pos = 0 #도착 예정 위치 
		
		#이동시키려는 말이 이미 도착했다면 pass
		if cur_pos == -1:
			continue

		#현재 위치가 파란색 화살표 위치이면 index 바꿈 
		if cur_pos == 5:
			cur_pos = 21
			move -= 1

		elif cur_pos == 10:
			cur_pos = 24
			move -= 1

		elif cur_pos == 15:
			cur_pos = 26
			move -= 1

		# 도착 예정 위치 탐색(파란색 화살표 위치에 도착하면 index 바꿈)
		if cur_pos < 21:
			nex_pos = cur_pos + move

		elif cur_pos >= 21 and cur_pos < 24:
			if cur_pos + (move) >= 24:
				nex_pos = 29 + (move - 3) 

			else:
				nex_pos = cur_pos + move
		
		elif cur_pos >= 23 and cur_pos < 26:
			if cur_pos + move >= 26:
				nex_pos = 29 + (move - 2)
			
			else:
				nex_pos = cur_pos + move
		else:
			nex_pos = cur_pos + move 

		if nex_pos == 32:
			nex_pos = 20
		
		#말이 도착하려는 위치가 종료 지점인 경우, 도착지점으로 말 이동		
		if (cur_pos < 21 and nex_pos >= 21) or (cur_pos >= 21 and cur_pos < 33 and nex_pos >= 33):
			cur_hor[i] = -1
			go(cur_hor, idx + 1, sums) 

		#도착 예정 지점에 다른 말이 없을 경우, 도착 지점으로 말 이동
		else:
			if nex_pos not in cur_hor:
				cur_hor[i] = nex_pos
				go(cur_hor, idx + 1, sums + yuts[nex_pos])

if __name__ == "__main__":
	#4개의 말 위치
	horses = [0] * 4 

	#윷놀이판 구하기
	yuts = list(2*i for i in range(21))

	#파란색 윷놀이판 더하기
	yuts.extend([13,16,19])
	yuts.extend([22,24])
	yuts.extend([28,27,26])
	yuts.extend([25,30,35])
	
	dices = list(map(int,input().split()))
	go(horses,0,0)
	print(max_sum)
