from itertools import combinations
def solution(relation):
    answer = 0
    columns = len(relation[0])# 컬럼의 개수
    
    listNew = [[] for i in range(columns)]
    for i in range(len(relation)):
        tmp = relation[i]
        for j in range(columns):
            listNew[j].append(tmp[j])
    print(listNew)
    
    candidate = [i for i in range(len(relation[0]))]
    result = []
    for num in range(1, columns+1):
        combs = list(combinations(candidate, num))
        print(combs)
        setTmp = set()
        for comb in combs:
            # 루프 돌면서 중복되는지 확인
            flag= 1
            for i in range(len(relation)):
                # 비교할 key
                key = ""
                for k in comb:
                    key += relation[i][k]
                for j in range(i+1, len(relation)):
                    # 비교할 대상key 만들기
                    dkey = ""
                    for k in comb:
                        dkey += relation[j][k]
                    if key == dkey:
                        flag=0
                        break
                if flag == 0:
                    break
            if flag == 1:
                print("f ",comb)
                result.append(comb)
                answer+=1
    # candidate 제거
    print("result:",result)
    i = 0
    while i < len(result):
        ori = result[i]
        tmp = []
        for j in range(i+1, len(result)):
            wrong = len(ori)
            for k in ori:
                if k in result[j]:
                    wrong-=1
            if wrong == 0: # 최소성 만족 안함
                tmp.append(result[j])
        print(tmp)
        # 제거하기
        for t in tmp:
            result.remove(t)
        i+=1
    print(result)
    return len(result)