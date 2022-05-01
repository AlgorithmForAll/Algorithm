import sys
input = sys.stdin.readline


def binary_search(start, end):
    while start < end:
        mid = (start+end)//2
    
        temp = 0
        for i in range(1, N+1):
            temp += min(mid//i, N)

        if K <= temp:
            end = mid
        else:
            start = mid+1
    return start
    

N = int(input())
K = int(input())

print(binary_search(1, K))