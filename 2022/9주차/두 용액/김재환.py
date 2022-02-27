"""
완탐으로 하면 100,000*100,000라서 너무 오래걸린다.
고로 투포인터로 푼다.
"""


N = int(input())
nums = list(map(int, input().split()))
nums.sort()
diff = 2000000000

L = 0
R = len(nums)-1

A, B = 0, 0
while L < R:
    ans = nums[L] + nums[R]
    if diff > abs(ans):
        diff = abs(ans)
        A = nums[L]
        B = nums[R]

    if ans > 0:
        R -= 1
    else:
        L += 1
print(A, B)
