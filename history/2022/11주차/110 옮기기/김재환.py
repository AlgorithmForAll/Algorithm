"""
진짜 어렵다;;;
https://studyandwrite.tistory.com/337

"""


def solution(s):
    answer = []

    for string in s:
        stack = []
        count = 0
        for w in string:
            # 110을 찾는다.
            if len(stack) >= 2 and w == '0' and stack[-1] == '1' and stack[-2] == '1':
                count += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(w)
        # 11인 경우를 찾아서 넣어준다.
        index = 0
        for i in stack[::-1]:  # 0 나오는거 뒤에 붙어야 한다.
            if '0' == i:
                break
            else:
                index += 1
        answer.append(
            "".join(stack[:len(stack)-index]) + "110"*count + "1"*index)

    return answer


solution(["1110", "100111100", "0111111010"])
