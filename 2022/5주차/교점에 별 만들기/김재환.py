def solution(line):
    answer = []
    s = set()
    miny = 100000000000
    minx = 100000000000
    maxy = -100000000000
    maxx = -100000000000
    for i in range(len(line)-1):
        A, B, E = line[i]
        for j in range(i+1, len(line)):
            C, D, F = line[j]
            if A*D - B*C == 0:
                continue
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            if (x).is_integer() and (y).is_integer():
                # x와 y의 최대최소 구하기
                maxx = int(max(x, maxx))
                minx = int(min(x, minx))
                maxy = int(max(y, maxy))
                miny = int(min(y, miny))
                s.add((int(y), int(x)))
    tmp = [["." for i in range(minx, maxx+1)] for i in range(miny, maxy+1)]
    for t in s:
        y, x = t
        tmp[-(y-(maxy))][x-(minx)] = "*"
    for t in tmp:
        answer.append("".join(t))
    return answer
