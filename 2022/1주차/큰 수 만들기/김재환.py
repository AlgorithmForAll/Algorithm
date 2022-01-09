"""
1. 스택 생성
2. number 문자열 끝까지 순회
3. stack 마지막 값보다 넣으려고 하는 값이 클 때
4. 삭제할 수 있는 값이 더 있으면 stack에서 popgkrh 삭제할 수 있는 값 하나 감소
5. 삭제할 수 있느 값 더이상 업승면 while문 종료
6. number 문자열 끝까지 다 순회했느데 아직 삭제해야할 개수가 더 남으면 마지막 부분 제거
https://velog.io/@dailyhyun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0
"""

def solution(number, k):
    answer = ''
    s = []
    
    for i in number:
        while s and i>s[-1]:
            if k > 0:
                s.pop()
                k-=1
            else:
                break
        s.append(i)        
    if k > 0 :
        for i in range(k):
            s.pop()
    return "".join(s)

"""
from itertools import combinations

def solution(number, k):
    answer = ''
    coms = list(combinations(list(number), len(number) - k))
    coms.sort()
    return "".join(coms[-1])
시간초과 남
def solution(number, k):
    answer = ''
    
    _number = list(number)
    _number.sort()
    # numMap 만들기
    numMap = {}
    for i in range(10):
        numMap[i]=0
    print("버릴값:",_number[:k])
    for i in _number[:k]:
        numMap[int(i)] += 1
    print(numMap)
    # 그리디 연산 시작
    for n in number:
        if numMap[int(n)] > 0:
            numMap[int(n)] -= 1
            continue
        else:
            answer += n
        
    return answer
값이 안맞음
"""

