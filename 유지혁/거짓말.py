import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    true_list = set(input().split()[1:])
    parties = []

    for _ in range(M):
        parties.append(set(input().split()[1:]))

    for _ in range(M):
        for party in parties:
            if party & true_list:
                true_list = true_list.union(party)

    cnt = 0
    for party in parties:
        if party & true_list:
            continue
        cnt += 1

    print(cnt)
