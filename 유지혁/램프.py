#1034 램프
# 한번에 한 열의 램프를 켜고/끌 수 있으며, K번 조절할 수 있을 때 모든 열이 다 켜져있는 행의 최대갯수

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int,input().split())
    arr = list(list(input().rstrip()) for _ in range(N))
    K = int(input())
    answer = 0

    for ith_arr in arr:
        zero_cnt = ith_arr.count('0') #ith_arr의 0개수 
        #0개수가 k보다 적고 2로 나눈 나머지가 같은 경우
        #ith_arr와 같은 0의 개수를 가진 행 탐색 
        if zero_cnt <= K and zero_cnt % 2 == K % 2:
            tmp_cnt = 0
            for jth_arr in arr:
                if ith_arr == jth_arr:
                    tmp_cnt += 1
            answer = max(answer,tmp_cnt)
    print(answer)
