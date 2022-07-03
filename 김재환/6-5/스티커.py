
"""
dp문제이며 dp에는 해당 스티커를 떼는 경우 최댓값을 구한다. 결과적으로 가장 큰 값을 구한다.

T <= 100,000
c <= 100

시간복잡도 : 200 * 100,000 = 20,000,000 낫밷
"""
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    score = []
    score.append(list(map(int, input().split())))
    score.append(list(map(int, input().split())))
    answer = max(score[0][0], score[1][0])
    for j in range(1, n):
        for i in range(2):
            big = 0
            if j != 1:
                big = max(big, score[i][j-2])
                big = max(big, score[i ^ 1][j-2])
            big = max(big,  score[i ^ 1][j-1])
            score[i][j] += big
            answer = max(answer, score[i][j])
    print(answer)
