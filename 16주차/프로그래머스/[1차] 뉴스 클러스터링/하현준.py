"""
[1차] 뉴스 클러스터링
https://programmers.co.kr/learn/courses/30/lessons/17677
"""


def jak(a, b):
    A = [a[i:i+2].lower() for i in range(len(a)-1) if a[i:i+2].isalpha()]
    B = [b[i:i+2].lower() for i in range(len(b)-1) if b[i:i+2].isalpha()]
    inter = []
    onlyA=[]
    
    for i in A:
        if i in B:
            B.remove(i)
            inter.append(i)
        else:
            onlyA.append(i)
    union = onlyA + inter + B
    print(inter)
    print(union)
    try:
        return len(inter)/len(union)
    except ZeroDivisionError:
        return 1


def solution(str1, str2):
    return int(jak(str1, str2) * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
