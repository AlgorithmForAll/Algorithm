#2504 괄호의 값
# stack
from collections import deque

def solution( st ):
	answer = 0
	s = deque() #stack

	for i in range(len(st)):
		x = st[i]
		if x == '(' or x == '[':
			s.append(x)

		elif x == ')':
			tmp = 0
			if len(s) == 0 or s[-1] == '[':
				return 0
			elif s[-1] == '(':
				tmp = 1
            #숫자가 있으면, '(' 가 나올때까지 숫자들을 더함
			else:
				tmp = int(s.pop())
				while len(s) != 0 and s[-1].isdigit() == True:
					tmp += int(s.pop())
				if len(s) == 0 or s[-1] == '[':
					return 0
			s.pop()
			s.append(str(tmp*2))

		elif x == ']':
			tmp = 0
			if len(s) == 0 or s[-1] == '(':
				return 0
			elif s[-1] == '[':
				tmp = 1
			else:
                #숫자가 있으면 '['가 나올 때까지 숫자들 더함 
				tmp = int(s.pop())
				while len(s) != 0 and s[-1].isdigit() == True:
					tmp += int(s.pop())
				if len(s) == 0 or s[-1] == '(':
					return 0
			s.pop()
			s.append(str(tmp*3))
	
	#stack에 괄호가 남아있는 경우 잘못된 괄호
	if len(s) == 0 :
		return 0
	elif  '(' in s or '[' in s:
		return 0

	answer = sum( list( int(x) for x in s) )
	return answer
		

if __name__ == "__main__":
	st = input()
	answer = solution(st)
	print(answer)
