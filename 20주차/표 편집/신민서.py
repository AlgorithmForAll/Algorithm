def solution(n, k, cmd):
    answer = ''
    stack = []
    llst = {0: [n-1, 1], n-1: [n-2, 0]}
    for i in range(1, n-1):
        llst[i] = [i-1, i+1]  #링크드리스트 생성
    for c in cmd:
        cc = c.split(' ')
        if cc[0] == 'D':
            num = int(cc[1])
            while num != 0:
                k = llst[k][1]
                num -= 1
        elif cc[0] == 'U':
            num = int(cc[1])
            while num != 0:
                k = llst[k][0]
                num -= 1
        elif cc[0] == 'C':
            tmp = llst[k]
            llst[llst[k][0]][1] = llst[k][1]
            llst[llst[k][1]][0] = llst[k][0]
            stack.append([k, llst[k]])
            del llst[k]
            if tmp[1] == 0:   #tmp의 다음게 0이면 (삭제되는게 마지막 원소이면)
                k = tmp[0]
            else:  #그렇지 않으면 다음걸 선택
                k = tmp[1]
        else:
            kk, lst = stack.pop()
            llst[lst[0]][1] = kk
            llst[kk] = [lst[0], lst[1]]  #kk가 링크드리스트에 없기 때문에 llst[kk][0] = lst[0]의 식으로 하는건 안된다.
            llst[lst[1]][0] = kk
    for i in range(n):
        if i in llst:
            answer += 'O'
        else:
            answer += 'X'
    return answer