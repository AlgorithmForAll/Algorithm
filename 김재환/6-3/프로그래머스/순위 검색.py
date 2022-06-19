def binSearch(num, score):
    L = 0
    R = len(num) - 1
    F = 0
    while -1 < L <= R:
        M = (L+R)//2
        if num[M] >= score:
            R = M - 1
            F = len(num) - M
        else:
            L = M + 1
    return F


LANG = ["cpp", "java", "python", "-"]
POSI = ["backend", "frontend", "-", ]
EXP = ["junior", "senior", "-"]
FOOD = ["chicken", "pizza", "-"]


def DFS(index, word, key, memo):
    if index == 4:
        memo.append(key)
    else:
        DFS(index+1, word, key+word[index], memo)
        DFS(index+1, word, key+"-", memo)


def DFS2(index,  key, d):
    if index == 4:
        d[key] = []
    if index == 0:
        for i in range(4):
            DFS2(index+1, key + LANG[i], d)
    elif index == 1:
        for i in range(3):
            DFS2(index+1,  key + POSI[i], d)
    elif index == 2:
        for i in range(3):
            DFS2(index+1,  key + EXP[i], d)
    elif index == 3:
        for i in range(3):
            DFS2(index+1,  key + FOOD[i], d)


def solution(info, query):
    answer = []

    D = {}
    DFS2(0, "", D)

    for i in info:
        word = i.split(" ")
        memo = []
        DFS(0, word, "", memo)
        for key in memo:
            if key in D:
                D[key].append(int(word[-1]))
            else:
                D[key] = [int(word[-1])]

    for key in D.keys():  # 미리 하지 않으면 많은 쿼리를 돌릴때마다 매번 정렬을 해줘야하기 때문에 미리 정렬
        D[key].sort()

    for q in query:
        word = q.split(" and ")
        foodScore = word.pop()
        food, score = foodScore.split(" ")
        key = "".join(word) + food
        scores = D[key]
        number = binSearch(scores, int(score))
        answer.append(number)
    return answer
