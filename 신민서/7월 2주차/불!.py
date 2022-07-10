"""
참고:
https://ywtechit.tistory.com/76
"""
def bfs(r, c):
    while qf:
        fx, fy = qf.pop(0)
        for k in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nfx, nfy = fx + k[0], fy + k[1]
            if 0 <= nfx < r and 0 <= nfy < c:
                if arr[nfx][nfy] != '#' and vf[nfx][nfy] == 0:
                    vf[nfx][nfy] = vf[fx][fy] + 1
                    qf.append([nfx, nfy])
    while qj:
        jx, jy = qj.pop(0)
        for k in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            njx, njy = jx + k[0], jy + k[1]
            if 0 <= njx < r and 0 <= njy < c:
                if not vj[njx][njy] and arr[njx][njy] != '#' and (vj[jx][jy] + 1 < vf[njx][njy] or not vf[njx][njy]):
                    vj[njx][njy] = vj[jx][jy] + 1
                    qj.append([njx, njy])
            else:
                return vj[jx][jy]
    return 'IMPOSSIBLE'


r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
qf = []
qj = []
vf, vj = [[0 for _ in range(c)] for __ in range(r)], [[0 for _ in range(c)] for __ in range(r)]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 'J':
            qj.append([i, j])
            vj[i][j] = 1
        elif arr[i][j] == 'F':
            qf.append([i, j])
            vf[i][j] = 1

print(bfs(r, c))