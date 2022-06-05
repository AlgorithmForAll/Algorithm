#1022 소용돌이 예쁘게 출력하기
#실패후 블로그 참고: 나중에 다시 풀기(https://ek12mv2.tistory.com/83), https://sangminlog.tistory.com/entry/boj-1022
import sys
input = sys.stdin.readline

def getValue(r,c):
	N = max(abs(r), abs(c))
	last = 2 * N + 1
	last = last ** 2

	if r == N: #아래 
		return last - (N-c)
	elif c == -N: #왼쪽 
		return last - (2 * N) - (N - r)
	elif r == -N:# 위
		return last - (4 * N) - (N + c)
	else: #오른쪽
		return last - (6 * N) - (N + r)

def getDigit(val):
		return len(str(val))

if __name__ == "__main__":
    r1, c1, r2, c2 = map(int,input().split())
    max_len = 0
    for y in range(r1,r2 + 1):
        for x in range(c1,c2 + 1):
            max_len = max(max_len, getDigit(getValue(y,x)))
    
    arr = []
    for y in range(r1, r2 + 1):
        for x in range(c1, c2 + 1):
            num = str(getValue(y,x))
            arr.append(num)
            print(num.rjust(max_len), end = ' ')
        print()
           
