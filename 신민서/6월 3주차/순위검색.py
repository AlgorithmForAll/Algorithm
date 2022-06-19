from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    infodesk = {} #만들 수 있는 모든 조합을 만들기 위해서 선언한 딕셔너리
    answer = []
    for inf in info:
        inff = inf.split() #띄어쓰기 기준으로 split 해준걸 inff 배열로 만듦.
        val = inff[-1] #inff의 마지막 원소가 점수. 점수를 val 변수에 넣어준다.
        inff = inff[:-1] #점수는 잘라냄. [java, backend, junior, pizza]
        for i in range(5): #만들 수 있는 모든 조합 다 만들어주기
            for c in combinations(inff, i):
                tmp = ''.join(c)
                #print(tmp)
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
        tmp = ''.join(quu) #query에서 -와 and 다 제거해주고 문장으로 합쳐준다.
        if tmp in infodesk:
            answer.append(len(infodesk[tmp]) - bisect_left(infodesk[tmp], int(val)))
        else: #info에 없는걸 query로 요구한경우 결과도 없기 때문에 0을 append 해준다.
            answer.append(0)
    return answer