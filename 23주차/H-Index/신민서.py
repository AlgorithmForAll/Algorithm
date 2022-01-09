def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(citations[n-1]):
        cnt = 0
        for j in range(n):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i and cnt > answer:
            answer = i
    return answer