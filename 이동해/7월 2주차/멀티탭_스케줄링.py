n, k = map(int, input().split())
orders = list(map(int, input().split()))

count = 0
tap = []
for i in range(k):
    # 1) 이미 멀티탭에 사용중인 경우
    if orders[i] in tap:
        continue

    # 2) 멀티탭 빈 공간이 있는 경우
    if len(tap) < n:
        tap.append(orders[i])
        continue
    
    # 3) 멀티탭에서 하나를 제거해야 하는 경우
    else:
        max_val = -1
        temp = orders[i + 1: k]
        
        for t in tap:
            # 3-1) 앞으로 사용하지 않는 경우
            if t not in temp:
                tap.remove(t)
                count += 1
                break
            # 3-2) 사용하는 경우
            else:
                max_val = max(max_val, temp.index(t))
        
        # break 안 걸렸으면         
        if len(tap) == n:
            tap.remove(temp[max_val])
            count += 1
        tap.append(orders[i])
print(count)

        
