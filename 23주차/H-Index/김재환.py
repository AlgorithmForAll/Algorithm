def binSearch(ci,num): # lowerbound
    index=len(ci)
    L = 0
    R = len(ci)
    F = 0 
    while L<R:
        M = (L+R)//2
        if num <= ci[M]: # 더 진행
            R = M
            index = M
        else: # 값 반환
            L = M+1    
    return index

def solution(citations):
    answer = 0
    citations.sort()    
    # h정의
    for h in range(10001):
        if h <= len(citations) - binSearch(citations, h):
            answer = h
        else:
            break
    print("bin:",binSearch(citations, 2))
    return answer