"""
110 옮기기
https://programmers.co.kr/learn/courses/30/lessons/77886
참고 : https://bladejun.tistory.com/153
holy shit~~

110을 가능한 0보다 뒤에, 1보다 앞에 위치하도록 한다.
"""
from collections import deque


def solution(s):
    answer = []
    for ss in s:
        print("-" * 40)
        print(ss)
        n = len(ss)
        count = 0
        stack = []
        for i in range(n):
            if ss[i] == "0":
                print(stack)
                if stack[-2:] == ["1", "1"]:
                    stack.pop()
                    stack.pop()
                    count += 1
                else:
                    stack.append(ss[i])
            else:
                stack.append(ss[i])

        if count == 0:
            answer.append(ss)
        else:
            print(stack)
            result = deque([])
            while stack:
                if stack[-1] == "1":
                    result.append(stack.pop())
                else:
                    break

            while count>0:
                count-=1
                result.appendleft("110")
            while stack:
                result.appendleft(stack.pop())

            print(result)
            answer.append("".join(result))
    return answer


print(solution(["1110", "100111100", "0111111010", "110011001100"]), ["1101", "100110110", "0110110111"])
