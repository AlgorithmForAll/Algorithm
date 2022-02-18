def intToBin(val):
    return bin(val)[2:]


def binToInt(strval):
    return int(strval, 2)


def removeZero(strval):
    result = ""
    for i in strval:
        if i == "1":
            result += "1"
    return result


def solution(s):
    answer = []
    count = 0
    zero = 0
    while True:
        # 1. 0 제거
        length = len(s)
        s = removeZero(s)
        zero += length - len(s)
        # 2. int로 만들기
        result = len(s)
        count += 1

        # 탈출조건 1만 존재할때
        if result == 1:
            break
        s = intToBin(result)
    return [count, zero]
