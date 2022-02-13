def solution(cacheSize, cities):
    answer = 0
    cache = [""]*cacheSize
    for _city in cities:
        city = _city.lower()
        if city in cache:
            answer += 1
            if len(cache) != 0:
                cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) != 0:
                cache.remove(cache[0])
            cache.append(city)
    if cacheSize == 0:
        answer = 5 * len(cities)
    return answer
