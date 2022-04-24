def bfs(nextword, visit, words, target):
    queue = []
    words.append(nextword)
    queue.append(len(visit) - 1)
    while queue != []:
        q = queue.pop()
        if target == words[q]:
            return visit[q]
        for i in range(len(visit)):
            cnt = 0
            for j in range(len(words[q])):
                if words[q][j] != words[i][j]:
                    cnt += 1
            if visit[i] == 0 and cnt == 1:
                visit[i] = visit[q] + 1
                queue.append(i)
    return 0


def solution(begin, target, words):
    answer = 0
    visit = [0] * (len(words) + 1)
    answer = bfs(begin, visit, words, target)
    return answer