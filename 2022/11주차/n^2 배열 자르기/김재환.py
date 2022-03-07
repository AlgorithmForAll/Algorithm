def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right+1)):
        y = i // n
        x = i % n
        answer.append(max(y+1, x+1))
    return answer
