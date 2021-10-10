def solution(sizes):
    answer = 0
    # 최댓값은 어딜가나 최댓값
    # 큰걸 한쪽으로 몰기, 그리고 양 방향 큰거 곱해서 곱구하기

    l = []
    r = []
    for i in sizes:
        a, b = i
        if a > b:
            l.append(a)
            r.append(b)
        else:

            l.append(b)
            r.append(a)
    answer = max(l) * max(r)

    return answer
