n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 가장 큰 수와 B의 가장 작은 수를 짝지어 계산
B.sort()
A.sort(reverse=True)

min_sum = 0
for a, b in zip(A, B):
    min_sum += a * b

print(min_sum)