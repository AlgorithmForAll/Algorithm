def solution(prices):
    result = [i for i in range(len(prices)-1, -1, -1)]
    s = [[0, prices[0]]]
    for pi in range(1, len(prices)):
        price = prices[pi]
        if len(s) > 0 and price >= s[-1][1]:
            s.append([pi, price])
        else:
            while True:
                if len(s) == 0 or s[-1][1] <= price:
                    break
                result[s[-1][0]] -= result[pi]
                s.pop()
            s.append([pi, price])
    return result


print(solution([9, 1]))
