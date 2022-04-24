from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    infodesk = {} #만들 수 있는 모든 조합을 만들기 위해서 선언한 딕셔너리
    answer = []
    for inf in info:
        inff = inf.split()
        val = inff[-1]
        inff = inff[:-1]
        for i in range(5): #만들 수 있는 모든 조합 다 만들어주기
            for c in combinations(inff, i):
                tmp = ''.join(c)
                if tmp in infodesk:
                    infodesk[tmp].append(int(val))
                else:
                    infodesk[tmp] = [int(val)]
    for k in infodesk:
        infodesk[k].sort() #infodesk의 키에 대한 value들 다 오름차순으로 정렬하기
    for q in query:
        qu = q.split() #배열로 만들어줘야 remove를 쓸 수 있다.
        while '-' in qu:
            qu.remove('-')
        while 'and' in qu:
            qu.remove('and')
        val = qu[-1]
        quu = qu[:-1]
        tmp = ''.join(quu)
        if tmp in infodesk: #cpp가 없는데 query에서 cpp를 요구하는 경우 infodesk의 키에 tmp가 없을 수 있다.
            answer.append(len(infodesk[tmp]) - bisect_left(infodesk[tmp], int(val)))
        else: #info에 없는걸 query로 요구한경우 결과도 없기 때문에 0을 append 해준다.
            answer.append(0)
    return answer