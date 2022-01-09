string = list(input())
boom = list(input())

stack = []
for ch in string:

    stack.append(ch)
    if stack[-1] == boom[-1]:
        # boom만큼 비교해보기
        if len(stack) >= len(boom) and stack[-len(boom):] == boom:
            for _ in range(len(boom)):
                stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
