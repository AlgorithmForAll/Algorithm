r1, c1, r2, c2 = map(int, input().split())
row = abs(r2 - r1 + 1)
col = abs(c2 - c1 + 1)
graph = [[0] * (col) for _ in range(row)]

def get_value(x, y):
    level = max(abs(x), abs(y))
    base_before = pow((level - 1) * 2 + 1, 2)
    base_now = pow((level * 2 + 1), 2)
    dx, dy = level - x, level - y

    if x >= y:
        return base_now - dx - dy
    else:
        return base_before + dx + dy

x, y = r1, c1
max_val = 0
for i in range(row):
    for j in range(col):
        graph[i][j] = get_value(x, y)
        max_val = max(graph[i][j], max_val)
        y += 1
    x = x + 1
    y = c1

max_len = len(str(max_val))
for i in range(row):
    for j in range(col):
        print(str(graph[i][j]).rjust(max_len, ' '), end = ' ')
    print() 