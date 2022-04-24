"""
https://pannchat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D-python
이사람은 이걸 도대체 어떻게 생각한 걸까.......
res : 결과적으로 보내줄 값
stack : 괄호, 연산자의 위치를 위해 미리 저장한다.
"""

line = list(input())

stack = []
answer = ""
for ch in line:
    if ch.isalpha():
        answer += ch
    else:
        if ch == "(":
            stack.append(ch)
        elif ch == "*" or ch == "/":
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(ch)
        elif ch == "+" or ch == "-":
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
while stack:
    answer += stack.pop()
print(answer)
