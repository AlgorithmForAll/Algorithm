"""
참고: https://velog.io/@imnotmoon/Python-%EB%B0%B1%EC%A4%80-1038.-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98
"""
n = int(input())
q = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 9
if n <= total: #구하려는게 9번째보다 같거나 작으면 그대로 q에서 찾아낸다.
    print(q[n])
    exit()
while q:  #그렇지 않은 경우에 q에서 하나씩 꺼내고 넣는 과정을 통해서 total을 찾아낸다.
    c = q.pop(0) #큐에서 하나씩 뺀다. c는 맨 앞자리 숫자를 말한다.
    for i in range(10):
        if i >= int(c[-1]): #뒤에 올 숫자가 c보다 크거나 같으면 더 루프를 돌 필요가 없어서 패스
            break
        q.append(c+str(i)) #그렇지 않으면 큐에 추가.
        total += 1
        if total == n:
            print(q[-1]) #total이 n과 같아졌을 때 큐의 마지막 숫자 print.
            exit()
print(-1)  #사실상 감소하는 수는 1022번째인 9876543210이 끝이기 때문에 그 다음의 숫자를 입력으로 넣으면 -1이 된다.

