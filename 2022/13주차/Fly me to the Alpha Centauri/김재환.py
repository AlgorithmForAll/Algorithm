"""
규칙을 모르겠으면 하나씩 잘 정리해서 써보자

"""
T = int(input())
print(T)
for t in range(T):
    a, b = map(int, input().split())
    print("a,b:", a, b)
    K = 0
    count = 0
    while a < b:
        diff = b-a
        if diff == 0:
            break

        if diff == K+1:
            count += 1
            break
        elif diff == K:
            count += 1
            break
        elif diff == K-1:
            count += 1
            break
        elif diff >= (K+1)*2 and (K+1) != 0:
            K += 1
            a += K
            b -= K
            count += 2
        elif diff >= K*2 and (K) != 0:
            a += K
            b -= K
            count += 2
        elif diff >= (K-1)*2 and (K-1) != 0:
            K += -1
            a += K
            b -= K
            count += 2
        print(a, b)
        print(diff, count)
    print(count)
