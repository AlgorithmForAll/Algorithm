"""
추석 트래픽
https://programmers.co.kr/learn/courses/30/lessons/17676
"""


def encode_time(data):
    h, m, s, ms = data[:2], data[3:5], data[6:8], data[9:]
    return int(ms) + (int(s) + int(m) * 60 + int(h) * 3600) * 1000


def solution(lines):
    answer = 0
    data = []
    start_time = encode_time(lines[0].split(" ")[1]) - int(float(lines[0].split(" ")[2][:-1]) * 1000) + 1

    for line in lines:
        line = line.split(" ")
        s = encode_time(line[1])
        t = int(float(line[2].replace("s", "")) * 1000)

        start = s - t - start_time + 1
        end = s - start_time
        if start < 0:
            start = 0
        data.append([start, end])

    for i in range(len(data)):
        for start in data[i]:
            count = 0
            end = start + 1000 - 1
            for j in range(i, len(data)):
                a, b = data[j]
                if end >= a:
                    count += 1
            answer = max(answer, count)
    return answer


print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))

print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
exit()
