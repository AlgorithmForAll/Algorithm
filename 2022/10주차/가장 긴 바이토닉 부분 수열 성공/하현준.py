"""
가장 긴 바이토닉 부분 수열
https://www.acmicpc.net/problem/11054
"""
import sys

sys.stdin = open("../input.txt")
input = sys.stdin.readline


def asc_lower_bound(target):
    lo = 0
    hi = len(asc_dp)
    while lo < hi:
        mid = (lo + hi) // 2
        if target <= asc_dp[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def desc_lower_bound(target):
    lo = 0
    hi = len(desc_dp)
    while lo < hi:
        mid = (lo + hi) // 2
        if target >= desc_dp[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    result = []
    asc_dp = [arr[0]]
    end = 0
    # asc
    for i in range(1, n):
        if asc_dp[-1] < arr[i]:
            asc_dp.append(arr[i])
            end = i
        elif asc_dp[-1] > arr[i]:
            # desc
            desc_dp = [asc_dp[-1]]
            for j in range(end + 1, n):
                if desc_dp[-1] > arr[j]:
                    desc_dp.append(arr[j])
                elif desc_dp[-1] < arr[j]:
                    index = desc_lower_bound(arr[j])
                    desc_dp[index] = arr[j]
            result.append(asc_dp + desc_dp[1:])

            index = asc_lower_bound(arr[i])
            asc_dp[index] = arr[i]
            end = i

    result.append(asc_dp)

    if result:
        print(len(max(result, key=len)))
    else:
        print(1)
