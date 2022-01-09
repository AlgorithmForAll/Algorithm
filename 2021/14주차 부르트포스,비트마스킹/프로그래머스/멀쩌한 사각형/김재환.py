"""
최대공약수로 하는게 무슨 연관성이 있는거지?
1. 패턴 찾기
2. 패턴내부의 규칙 찾기
3. 패턴의 개수만큼 곱하기
=> h+w-최대공약수
"""

def calc(w, h):
    if h == 0:
        return w
    return calc(h, w % h)


def solution(w, h):
    answer = 1
    # 기울기 식 구하기
    # y = -h/w + h
    # 최대 공약수 구하기
    if w > h:
        t = calc(w, h)
    else:
        t = calc(w, h)
    return w*h-(w+h-t)
