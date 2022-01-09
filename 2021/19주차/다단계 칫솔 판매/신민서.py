import math
def calculate(money, number, parents, answer):
    if parents[number] == number or money//10 == 0:
        answer[number] += money
        return
    send = money//10
    answer[number] += money - send
    calculate(send, parents[number], parents, answer)

def solution(enroll, referral, seller, amount):
    dict = {} #참여자마다 번호를 부여해준다.
    n = len(enroll)
    parents = [0] * (n+1) #누구의 부모일지 결정
    answer = [0] * (n+1)
    for i in range(n):
        dict[enroll[i]] = i+1
    for i in range(n):
        if referral[i] != "-":
            parents[i+1] = dict[referral[i]] #자식은 중복될 수 있지만 부모는 그럴 수 없단걸 활용. dict를 사용해서 트리 구조 생성.
    for i in range(len(seller)):
        calculate(amount[i]*100, dict[seller[i]], parents, answer)
    answer.pop(0)
    return answer