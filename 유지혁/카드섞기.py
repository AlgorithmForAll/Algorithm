#1091 카드섞기
# 구현 
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    P = list(map(int,input().split()))
    S = list(map(int,input().split()))
    ori = P[:N+1]
    mix = [i for i in range(N)]
    answer = 0

    while True:
        flag = False
    
        for i in range(N):
            if mix[i] % 3 != ori[i]:
                answer += 1
                temp = []
            
                for j in range(N):
                    if S[mix[j]] != j:
                        flag = True
                    temp.append(S[mix[j]])
                mix = temp
                break
        else:
            break
           
        if flag == False:
            answer = -1
            break

    print(answer)
