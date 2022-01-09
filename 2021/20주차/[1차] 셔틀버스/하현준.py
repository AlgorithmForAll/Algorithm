"""
[1차] 셔틀버스
https://programmers.co.kr/learn/courses/30/lessons/17678
"""


def upper_bound(arr, target):
    lo = 0
    hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search(arr, end, m):
    lo = 0
    hi = end + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        index = upper_bound(arr, mid)
        # print(index, encode(mid), index < m)
        if index < m:
            lo = mid
        else:
            hi = mid
    # print("-", lo, encode(lo))
    return lo


def decode(data):
    return int(data[3:]) + int(data[:2]) * 60


def encode(data):
    h = data // 60
    m = (data - h * 60)
    return f"{h:02}:{m:02}"


def solution(n, t, m, timetable):
    answer = -float('inf')
    data = sorted([decode(x) for x in timetable])
    start = decode("09:00")  # 540

    # print("-" * 40)
    for i in range(n):
        if not data:
            break

        bus = start + t * i
        # print(f"bus={encode(bus)} {m=}", [encode(x) for x in data])
        con_time = search(data, bus, m)
        answer = max(answer, con_time)

        stop = upper_bound(data, bus)
        a = data[:stop]
        b = data[stop:]
        data = a[m:] + b

    return encode(answer)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]), "09:00")
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]), "09:09"
      )
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]), "08:59"
      )
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]), "00:00"
      )
print(solution(1, 1, 1, ["23:59"]), "09:00"
      )
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]), "18:00"
      )
print(solution(3, 10, 2, ["09:10", "09:09", "09:10", "09:09", "09:09", "08:00", "08:00", "08:00"]))
