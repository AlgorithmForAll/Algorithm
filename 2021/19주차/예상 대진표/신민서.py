"""
Created by MinSeo on 2021/09/18.
Copyright ⓒ 2021 MinSeo Shin. All rights reserved.

"""
def solution(n,a,b):
    answer = 0
    while a != b:
        if a%2 == 1:
            a += 1
        if b%2 == 1:
            b += 1
        a = a//2
        b = b//2
        answer += 1
    return answer

