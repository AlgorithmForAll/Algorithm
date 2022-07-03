def bfs(start, end):
    q = []
    visited = [False for _ in range(100001)]
    saving = [0 for _ in range(100001)] #이전에 무슨 숫자였는지 저장
    visited[start] = True
    q.append(start)
    while q:
        x = q.pop(0)
        if x == k:
            break
        if x-1 >= 0 and not visited[x-1]:
            visited[x-1] = True
            saving[x-1] = x
            q.append(x-1)
        if x+1 <= 100000 and not visited[x+1]:
            visited[x+1] = True
            saving[x+1] = x
            q.append(x+1)
        if x*2 <= 100000 and not visited[x*2]:
            visited[x*2] = True
            saving[x*2] = x
            q.append(x*2)
    answer = [end]
    while end != start:
        end = saving[end]
        answer.insert(0, end)
    return answer


n, k = map(int, input().split())
answer = bfs(n, k)
print(len(answer) - 1)
for a in answer:
    print(a)