"""
백트래킹 냄새남

"""
N = int(input())
ctm = []
priList = set()
for n in range(N):
    price, deli = map(int, input().split())
    priList.add(price)
    ctm.append([price, deli])
_priList = list(priList)
_priList.sort(reverse=True)

final = 0
answer = 10**6

for val in _priList:
    total = 0
    for i in range(len(ctm)):
        price, deli = ctm[i]
        if val <= price and deli <= val:
            total += val-deli
    if total >= final:
        final = total
        answer = val

if final == 0:
    print(0)
else:
    print(answer)
