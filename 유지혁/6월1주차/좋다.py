#1253 좋다
#어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 좋은 수가 된다.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    answer = 0
    #i번째 수가 좋은 수인지 탐색 
    for i in range(N):
        num = arr[i]
        tmp = arr[:i] + arr[i+1:] #본인은 제외하는 arr
        left = 0
        right = len(tmp) - 1
        while left < right :
            s = tmp[left] + tmp[right]
            if s == num:
                answer += 1
                break
            elif num > s:
                left += 1
            elif num < s:
                right -= 1

    print(answer)
