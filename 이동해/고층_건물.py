n = int(input())
building = list(map(int, input().split()))
num = len(building)
count_list = []

# 전체 건물 확인
for i in range(num):
    x1 = i + 1
    y1 = building[i]
    count = 0

    # 왼쪽
    slope = None
    for l in range(i-1, -1, -1):
        x2 = l + 1
        y2 = building[l]
        cur_slope = (y2 - y1) / (x2 - x1)
        if (slope is None) or (cur_slope < slope):
            slope = cur_slope
            count += 1
    
    # 오른쪽
    slope = None
    for r in range(i+1, num):
        x2 = r + 1
        y2 = building[r]
        cur_slope = (y2 - y1) / (x2 - x1)
        if (slope is None) or (cur_slope > slope):
            slope = cur_slope
            count += 1
            
    count_list.append(count)
print(max(count_list))