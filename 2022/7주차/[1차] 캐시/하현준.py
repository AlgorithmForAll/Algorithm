"""
[1차] 캐시
https://programmers.co.kr/learn/courses/30/lessons/17680
"""


def solution(cacheSize, cities):
    answer = 0
    cache = dict()
    for time, city in enumerate(cities):
        city = city.lower()
        if city in cache and cacheSize > 0:  # cache hit
            cache[city] = time
            answer += 1
        else:  # cache miss
            answer += 5
            if not cache or len(cache) < cacheSize:
                cache[city] = time
            elif len(cache) == cacheSize:  # LRU
                data = sorted(list(cache.items()), key=lambda x: -x[1])
                data.pop()
                cache = dict(data)
                cache[city] = time
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 50)
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]), 21)
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]), 60)
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]), 52)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]), 16)
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]), 25)
print(solution(0, ["Jeju", "Jeju"]), 10)
