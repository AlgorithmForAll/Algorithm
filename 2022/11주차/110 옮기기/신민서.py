def solution(s):
    answer = []
    for ss in s:
        count = 0
        stack = "" #stack을 문자열로 선언해버리기
        for sss in ss:
            stack += sss
            if len(stack) >= 3:
                if stack[-1] == '0' and stack[-2] == '1' and stack[-3] == '1':
                    stack = stack[:-3]
                    count += 1
        idx = stack.rfind('0') #rfind: 반대로 끝부터 인덱스 찾게해주는 것.
        if idx == -1:
            stack = "110" * count + stack
        else:
            stack = stack[:idx+1] + "110" * count + stack[idx+1:]
        answer.append(stack)
    return answer