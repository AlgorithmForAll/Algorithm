"""
블로그(https://leedakyeong.tistory.com/135#comment16270807) 풀이 참고
- 최대공약수 g
- 잘라지는 사각형 수는 g*((w//g)+(h//g)-1) = w+h-g
"""
from math import gcd
def solution(w,h):
    return w*h - (w+h-gcd(w,h))



"""
처음 잘못생각했던 코드
예제만 보고 대각선 길이의 올림만큼 사각형 잘리는 것이라 생각했음
"""
from math import gcd, sqrt, ceil

def solution(w,h):
    answer = 1

    g = gcd(w,h)
    new_w = int(w//g)
    new_h = int(h//g)
    line = ceil(sqrt(new_h*new_h + new_w*new_w))
    answer = w*h - line*g

    return answer