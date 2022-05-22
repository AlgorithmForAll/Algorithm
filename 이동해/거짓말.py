n, m = map(int, input().split())
# 진실을 아는 사람(사람 수 제외)
true_people = set(input().split()[1:])

# 각 파티에 오는 사람(사람 수 제외)
party_list = []
for _ in range(m):
    party_list.append(set(input().split()[1:]))

for _ in range(m):
    for party in party_list:
        if party & true_people:
            true_people = true_people | party

count = 0
for party in party_list:
    if party & true_people:
        continue
    count += 1
print(count)
    