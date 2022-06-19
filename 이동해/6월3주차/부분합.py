n, s = map(int, input().split())   
numbers = list(map(int, input().split()))

INF = int(1e9)
length = INF
temp = 0
start, end = 0, 0

while True:
    if temp >= s:
        length = min(length, end - start)
        temp -= numbers[start]
        start += 1
    elif end == n:
        break
    else:
        temp += numbers[end]
        end += 1
    
if length != INF:
    print(length)
else:
    print(0)