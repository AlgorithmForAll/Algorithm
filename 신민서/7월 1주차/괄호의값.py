"""
참고:
https://mjmjmj98.tistory.com/70
"""
stack = []
s = input()

tmp = 1
answer = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
        tmp *= 2
    elif s[i] == '[':
        stack.append('[')
        tmp *= 3
    elif s[i] == ')':
        if stack and stack[-1] == '(':
            if s[i-1] == '(':
                answer += tmp
            tmp //= 2
            stack.pop()
        else:
            print(0)
            exit(0)
    elif s[i] == ']':
        if stack and stack[-1] == '[':
            if s[i - 1] == '[':
                answer += tmp
            tmp //= 3
            stack.pop()
        else:
            print(0)
            exit(0)
if stack:
    print(0)
else:
    print(answer)