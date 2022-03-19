"""
스킬트리
https://programmers.co.kr/learn/courses/30/lessons/49993
"""


def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    data = dict(zip(list(skill), [i for i in range(n)]))
    for skill_tree in skill_trees:
        stack = [-1]
        for st in skill_tree:
            if st in data:
                stack.append(data[st])
                if stack[-1] - stack[-2] != 1:
                    break
        else:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]), 2)
