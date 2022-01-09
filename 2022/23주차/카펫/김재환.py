def solution(brown, yellow):
    answer = []
    
    whSum = (brown + 4) // 2
    
    tmp = []
    # 가능한 가로 세로 구하기
    for i in range(whSum-1, whSum//2-1,-1):
        tmp.append([i,whSum-i])
    # 가능한지 판별
    for t in tmp:
        w,h = t
        if (w-2)*(h-2)== yellow:
            answer = [w,h]
            break    
    return answer