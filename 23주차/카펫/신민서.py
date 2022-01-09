def solution(brown, yellow):
    answer = []
    br = (brown + 4) // 2
    for x in range(1, br):
        y = br - x
        if (x-2)*(y-2) == yellow :
            a = max(x, y)
            b = min(x, y)
            answer.append(a)
            answer.append(b)
            break
    return answer