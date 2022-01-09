def solution(gems):
    answer = []
    gemSet = set(gems)
    # map
    map = {}
    for gem in gemSet:
        map.setdefault(gem, 0)
    print(map)

    L = 0
    R = 0
    flag = 0
    count = 0
    while R < len(gems):
        # add R index

        rVal = gems[R]
        if map[rVal] == 0:  # new gems
            flag += 1
        map[rVal] += 1
        count += 1
        R += 1
        # check result
        if flag == len(gemSet):
            answer.append([count, L+1, R, ])

        # check L value while
        while True:
            lVal = gems[L]
            # if rVal
            if map[lVal] > 1:
                map[lVal] -= 1
                count -= 1
                L += 1
            else:
                break
        # check result
        if flag == len(gemSet):
            answer.append([count, L+1, R])
    _answer = sorted(answer)
    _answer[0][1:]
    return _answer[0][1:]


#solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	)
solution(["2", "1", "1", "1", "1", "1", "3", "4", "1", "1", "2", "3", "4"]	)
