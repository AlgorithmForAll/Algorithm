def solution(people, limit):
    answer = 0
    # 보자마자 그리디 생각남
    people.sort()
    print(people)
    L = 0
    R = len(people)-1
    count = 0
    while L <= R:
        if people[L] + people[R] > limit:
            R -= 1
        else:
            L += 1
            R -= 1
        count += 1
    print(count)

    return count
