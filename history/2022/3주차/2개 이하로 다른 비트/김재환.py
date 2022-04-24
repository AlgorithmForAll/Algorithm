def solution(numbers):
    answer = []

    for a in numbers:
        answer.append(bit(a))
    return answer


def bit(number):
    if number % 2 == 0:  # 짝수
        return number+1
    else:
        bl = list("0"+bin(number)[2:])
        for i in range(len(bl)-1, -1, -1):
            if bl[i] == '0':
                bl[i] = '1'
                bl[i+1] = '0'
                break
        return int("".join(bl), 2)
