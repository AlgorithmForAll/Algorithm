import heapq

def solution(operations):
    answer = []
    bigQ = []
    smallQ = []

    for operation in operations:
        op,num = operation.split(' ')
        if op == 'I':# 삽입
            heapq.heappush(bigQ, -int(num))
            heapq.heappush(smallQ, int(num)) # heapq 자체가 최소힙으로 작동한다.
        else: # 제거
            if num == '1' and len(bigQ)!=0: # 최댓값 제거 
                big = -heapq.heappop(bigQ)
                smallQ.remove(big)
            elif num =='-1' and len(smallQ)!=0: # 최솟값 제거
                small = heapq.heappop(smallQ)
                bigQ.remove(-small)
    # 마지막에 각 큐에서 최댓값, 최솟값을 뽑아온다.
    big = 0
    small = 0
    if len(bigQ) != 0:
        big = -heapq.heappop(bigQ)
    if len(smallQ) !=0:
        small = heapq.heappop(smallQ)
    print([big,small])
    return [big, small]