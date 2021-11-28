def solution(info, query):
    data = dict()
    # 예전에는 4차원 배열을 만들었는데 그럴 필요가 없음
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list()) # 모든 경우의 수를 리스트로 초기화
                    # 튜플로 넣으면 문자열에 대한 처리가 필요 없어져서 좋은듯
    
    # 조건에 맞는 값을 넣는다. 키는 튜플로 넣어줌
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
    # 데이터를 하나씩 뽑아서 순서를 정렬한다.
    for k in data:
        data[k].sort()
    
    # 결과를 담을 배열 선언
    answer = list()

    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:# 이분탐색으로 해당 값보다 큰 경우의 수를 구한다.
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)
    print(answer)
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
         )
