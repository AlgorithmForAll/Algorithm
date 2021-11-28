"""
다단계 칫솔 판매
https://programmers.co.kr/learn/courses/30/lessons/77486
"""
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    rdata = dict()
    cdata = defaultdict(int)

    for i in range(len(referral)):
        rdata[enroll[i]] = referral[i]

    for i in range(len(seller)):
        who, cost = seller[i], amount[i] * 100

        while True:
            if who == "-":
                cdata[who] += cost
                break
            if cost * 0.1 < 1.0:
                cdata[who] += cost
                break

            ten_perc = int(cost * 0.1)
            cost -= ten_perc
            cdata[who] += cost
            cost = ten_perc
            who = rdata[who]
    for i in range(len(enroll)):
        answer.append(cdata[enroll[i]])
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
