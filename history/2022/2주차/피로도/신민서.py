import itertools

def solution(k, dungeons):
    answer = -1
    arr = []
    for i in range(len(dungeons)):
        arr.append(i)
    for l in list(itertools.permutations(arr)):
        kk = k
        cnt = 0
        for i in l:
            if kk >= dungeons[i][0]:
                kk -= dungeons[i][1]
                cnt += 1
            else:
                break
        answer = max(cnt, answer)
    return answer