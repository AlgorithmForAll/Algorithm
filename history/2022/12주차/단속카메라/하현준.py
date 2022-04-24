"""
단속카메라
https://programmers.co.kr/learn/courses/30/lessons/42884
ㅎㄷㄷ
"""


def solution(routes):
    count = 0
    n = len(routes)
    routes.sort(key=lambda x: x[1])
    check = set()
    for i in range(n):
        if i not in check:
            rin, rout = routes[i]
            temp = set()
            for j in range(n):
                if routes[j][0] <= rout <= routes[j][1]:
                    temp.add(j)

            check |= temp
            count += 1
            if len(check) == n:
                break
    return count


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]), 2)
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3], [-14, -13]]), 3)
