#1015 수열정렬
#P배열 : A배열의 원소 크기 순서를 저장한 배열  

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))


    #A 배열의 각 원소가 몇번째로 작은 값인지를 저장하는 배열 생성
    P = [-1] * N 
    sorted_A = sorted(A)

    for i in range(N):
        val = sorted_A[i]
        idx = A.index(val)
        P[idx] = i
        A[idx] = -1
    
    for x in P:
        print(x,end = ' ')
