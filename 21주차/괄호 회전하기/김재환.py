def check(string):
    sList = list(string)
    stack = [sList[0]]
    i = 1
    while i < len(string):
        if sList[i] == '[' or sList[i] == '{' or sList[i] == '(':
            stack.append(sList[i])
        else:
            if len(stack) != 0:
                if sList[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif sList[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif sList[i] == ']' and stack[-1] == '[':
                    stack.pop()
        i += 1
    if len(stack) != 0:
        return False
    else:
        return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        string = s[i:] + s[0:i]
        if check(string):
            answer += 1
    return answer
