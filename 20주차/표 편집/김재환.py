def solution(n, k, cmd):
    answer = ''
    # 초기값 list만들기
    result = ['O' for i in range(n)]
    table = {i: [i-1, i+1] for i in range(n)}
    stack = []
    # cmd 처리
    index = k
    count = 0
    for c in cmd:
        count += 1
        cl = c.split(' ')
        if cl[0] == 'D':  # D와 C는 인덱스 변경
            for i in range(int(cl[1])):
                index = table[index][1]
        elif cl[0] == 'U':
            for i in range(int(cl[1])):
                index = table[index][0]
        elif cl[0] == 'C':
            prev, back = table[index]
            stack.append(index)
            result[index] = 'X'
            if back == n:  # 마지막행인경우 index가 한칸 위로
                table[prev][1] = back
                index = prev
            else:
                if prev != -1:
                    table[prev][1] = back
                if back != n:
                    table[back][0] = prev
                index = back
        else:
            val = stack.pop()
            prev, back = table[val]
            if prev != -1:
                table[prev][1] = val
            if back != n:
                table[back][0] = val
            result[val] = 'O'
    return "".join(result)


#solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]	)
solution(8, 2, ["D 2", "C", "U 3", "C", "D 4",
         "C", "U 2", "Z", "Z", "U 1", "C"])

"""def solution(n, k, cmd):
    answer = ''
    # 초기값 list만들기
    table = [i for i in range(n)]
    stack = []
    # cmd 처리
    index = k
    count = 0
    for c in cmd:
        count += 1
        cl = c.split(' ')
        if cl[0] == 'D':  # D와 C는 인덱스 변경
            index += int(cl[1])
            print("D->", index)
        elif cl[0] == 'U':
            index -= int(cl[1])
            print("U->", index)
        elif cl[0] == 'C':
            absolute = table[index]
            stack.append([index, absolute])
            table.remove(table[index])
            if index == len(table)-1:  # 마지막행인경우 index가 한칸 위로
                index -= 1
                print("last C ->", index)
            else:  # 일반 행인 경우 index 그대로
                print("C ->", index)
        else:
            print("Z")
            relation, absolute = stack.pop()
            table.insert(relation, absolute)
        print("count:", count, "/", table)
    # stack을 통해 result처리
    result = ['O' for i in range(n)]
    for s in range(len(stack)):
        relation, absolute = stack.pop()
        result[absolute] = 'X'
    answer = "".join(result)
    print(answer)
    return answer
"""
