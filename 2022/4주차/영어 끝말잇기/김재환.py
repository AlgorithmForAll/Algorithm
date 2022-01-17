def solution(n, words):
    answer = []

    M = {}
    flag = 0
    index = 1
    M[words[0]] = 1
    for wi in range(1, len(words)):
        word = words[wi]
        index += 1
        if word in M or word[0] != words[wi-1][-1]:
            flag = 1
            break
        else:
            M[word] = 1
    if flag == 0:
        return [0, 0]
    failnum = index % n
    failindex = index // n
    if failnum == 0:
        failnum = n
    else:
        failindex += 1
    # 가장 먼저 탈락하는 사람 번호, 그 사람이 몇번째에 탈락
    return [failnum, failindex]
