#14002 가장 긴 증가하는 부분수열 4
# dp
# int형 리스트를 ' '.join시 map()으로 str 바꾸기

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int,input().split()))
    dp = [ 1 for _ in range(N)]

    #가장 긴 증가하는 부분수열의 길이
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

    #가장 긴 증가하는 부분수열
    arr = []
    max_dp =  max(dp)
    for i in range(N-1,-1,-1):
        if dp[i] == max_dp:
            arr.append(nums[i])
            max_dp -= 1

    arr.reverse()
    print(' '.join(map(str,arr)))
