def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        temp = city.lower()
        if temp not in cache:
            if len(cache) >= cacheSize and cacheSize != 0:
                cache.pop(0)
            if cacheSize != 0:
                cache.append(temp)
            answer += 5
        else:
            answer += 1
            cache.pop(cache.index(temp))
            cache.append(temp)
    return answer