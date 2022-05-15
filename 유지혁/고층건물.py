#1027 고층건물
# 가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력

# idx보다 왼쪽에서 볼 수 있는 빌딩 개수를 구하는 함수
def getCntLeft(idx):
    minSlope = float('INF') 
    cnt = 0 

    for i in range(idx-1, -1, -1):
        slope = (buildings[idx] - buildings[i]) / (idx - i) 

        # 이전의 최소 기울기보다 더 작아졌을 경우 update
        if minSlope > slope: 
            minSlope = slope
            cnt += 1

    return cnt


# idx보다 오른쪽에서 볼 수 있는 빌딩 개수를 구하는 함수
def getCntRight(idx):
    maxSlope = -float('INF') 
    cnt = 0 

    for i in range(idx+1, N):
        slope = (buildings[idx] - buildings[i]) / (idx - i) 

        # 이전의 최소 기울기보다 더 커졌졌을 경우 update
        if maxSlope < slope:
            maxSlope = slope
            cnt += 1

    return cnt


if __name__ == '__main__':
    N = int(input())  
    buildings = list(map(int, input().split()))

    answer = 0
    for i in range(N):
        left = getCntLeft(i)
        right = getCntRight(i)
        answer = max(answer, left + right)

    print(answer)
