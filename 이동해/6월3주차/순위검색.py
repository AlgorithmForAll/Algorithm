def solution(info, query):
    answer = []
    for q in query:
        q = q.replace('and', '')
        q = q.split()
        count = 0
        for i in info:
            i = i.split()
            flag = True
            if int(i[4]) < int(q[4]):
                flag = False
            else:
                for idx in range(4):
                    if q[idx] == '-':
                        continue
                    if q[idx] != i[idx]:
                        flag = False
                        break
            if flag:
                count += 1
        answer.append(count)
    return(answer)