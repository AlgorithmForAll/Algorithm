"""
회의가 일찍 끝나는 것을 찾으면 된다.
뒤에 정렬 왜붙은거지?
"""
import sys
input = sys.stdin.readline

N = int(input())
confs = []
for i in range(N):
    a, b = map(int, input().split())
    confs.append([a, b])
confs.sort(key=lambda x: (x[1], x[0]))

end = 0
count = 0
for conf in confs:
    a, b = conf
    if end <= a:
        end = b
        count += 1
        print(conf)
print(count)
