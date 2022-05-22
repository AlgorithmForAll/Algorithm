"""
알고리즘 분류 보고 풂
그리디 + 최소힙
강의시간이 존재할때 힙에 리스트형태로 강의실의 사용시간을 기재하여
가장 빨리 끝나는 강의실을 사용할 수 있도록 구현
"""
import heapq
import sys
input = sys.stdin.readline  # N <= 200000 이므로 입력받는 숫자가 크기 때문에 선언
N = int(input())
hq = []  # 강의실을 저장할 hq
cl = []  # 강의시간을 받는 리스트
for n in range(N):
    a, b = map(int, input().split())
    cl.append([a, b])
cl.sort()  # 모든 강의실을 받은 후에 가장 빨리 시작하는 순으로 정렬

for c in cl:
    a, b = c  # 강의의 시작시간 a, 강의의 종료시간 b
    if len(hq) == 0:
        heapq.heappush(hq, [b, a])
        continue

    # 강의실중 가장 끝나는 시간이 빠른경우를 뽑아온다. 이때 hq에 들어가는 인자는 [강의종료, 강의시작]
    end, start = heapq.heappop(hq)
    if end <= a:
        heapq.heappush(hq, [b, start])  # 강의실을 사용할 수 있는 경우 시간을 누적하여 hq에 선언
    else:
        # 강의실을 사용할 수 없는 경우 기존에 pop한 강의실을 넣어 원상복구
        heapq.heappush(hq, [end, start])
        heapq.heappush(hq, [b, a])  # 강의실을 사용할 수 없기 때문에 새로운 강의실을 추가해준다.
print(len(hq))
