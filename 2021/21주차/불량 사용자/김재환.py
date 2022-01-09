def checkId(user, banner):
    if len(user) != len(banner):
        return False
    for i in range(len(user)):
        if banner[i] == '*':
            continue
        elif banner[i] == user[i]:
            continue
        else:
            return False
    return True


def DFS(banList, i, com, result):
    if i == len(banList):
        result.add(tuple(sorted(com)))
        return
    for t in banList[i]:
        if t in com:
            continue
        _com = com + [t]
        DFS(banList, i+1, _com, result)


def solution(user_id, banned_id):
    answer = 0
    banList = [[] for i in range(len(banned_id))]
    # get
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if checkId(user_id[j], banned_id[i]):
                banList[i].append(user_id[j])
    print(banList)
    # combination
    result = set()
    print(DFS(banList, 0, [], result))
    print(result)

    return len(result)
