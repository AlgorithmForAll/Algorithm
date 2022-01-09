"""
짝지어 제거하기
https://programmers.co.kr/learn/courses/30/lessons/12973
참고 : https://eda-ai-lab.tistory.com/492

문자열 비교 ? -> stack 활용
"""


def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution("baabaa"))
print(solution("baaabaabcccacabb"))
print(solution("cdcd"))
