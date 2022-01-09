"""
비트마스킹이 어디 쓰일지 감이 잡히지 않아
블로그(https://peisea0830.tistory.com/35) 코드를 이해함
"""
import sys, itertools

# n, m 입력
n,m = map(int, sys.stdin.readline().split())

# words : 각 단어의 비트마스킹한 정수를 저장
words = [0] * n
ans = 0
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    # word 배열에 각 문자의 비트마스킹 저장
    for x in temp:
        words[i] |= (1 << (ord(x) - ord('a')))
        
# 만일 m이 5미만이면 필수 글자를 다 배울 수 없기 때문에 한 단어도 읽지 못한다
if m < 5:
    print(0)
else:
    # candidiate : 필수 글자를 제외한 알파벳
    # need : 필수 알파벳
    candidiate = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    need = ['a','c','t','i','n']
    for i in list(itertools.combinations(candidiate, m - 5)):
        each = 0
        res = 0
        # 각 조합에 대한 비트마스킹
        for j in need:
            each |= (1 << (ord(j) - ord('a')))
        for j in i:
            each |= (1 << (ord(j) - ord('a')))
            
        # 단어와 각 조합의 비교
        for j in words:
            if each & j == j:
                res += 1
                
        # 최대값 갱신
        if ans < res:
            ans = res
    print(ans)



"""
지난주와 같은 코드.
어디에서 비트마스킹이 쓰여야 하는지, 어떻게 더 시간을 줄여야 하는지 이해하지 못함
"""
from itertools import combinations

def solution(n,k):
    words = list()
    antatica = set(map(str, 'antatica'))
    for _ in range(n):
        w = set(map(str, input()))
        word = list(w - antatica)
        words.append(word)
    
    if k<5:
        return 0
    k -= 5
    alpabet = set(map(lambda x:chr(x), range(ord('a'), ord('z')+1))) - antatica
    combs = combinations(alpabet, k)
    result = 0
    for comb in combs:
        cnt = 0
        for w in words:
            if set(comb) & set(w) == set(w):
                cnt += 1
        result = max(result, cnt)

    return result