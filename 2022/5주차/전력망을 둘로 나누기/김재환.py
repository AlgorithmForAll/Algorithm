def DFS(n,start, adj, visited):
    s = [start]
    count = 1
    while s:
        t = s.pop()
        for nextNode in range(1,n+1):
            if adj[t][nextNode] == 1 and visited[nextNode]==0:
                s.append(nextNode)
                visited[nextNode] = 1
                count+=1
    return count
    

def solution(n, wires):
    answer = 100
    adj = [[0 for i in range(n+1)] for i in range(n+1)]
    for w in wires:
        a,b = w
        adj[a][b] = 1
        adj[b][a] = 1
    
    # wire를 하나씩 제거해본다.
    for w in wires:
        a,b = w
        adj[a][b] = 0
        adj[b][a] = 0
        # DFS로 연산해보기
        visited = [ 0 for i in range(n+1)]
        result = []
        for i in range(1,n+1):
            if visited[i]==0:
                visited[i]=1
                result.append(DFS(n,i,adj,visited))
        diff = abs(result[0] - result[1])
        answer = min(diff,answer)
    
        adj[a][b] = 1
        adj[b][a] = 1
    
    return answer