"""
광고 삽입
https://programmers.co.kr/learn/courses/30/lessons/72414
"""


def decode_time(data):
    data = data.split(":")
    return int(data[2]) + int(data[1]) * 60 + int(data[0]) * 3600


def encode_time(data):
    h = data // 3600
    m = (data - h * 3600) // 60
    s = data - h * 3600 - m * 60
    return f"{h:02}:{m:02}:{s:02}"


def solution(play_time, adv_time, logs):
    total = decode_time(play_time)
    adv = decode_time(adv_time)
    cumul_data = [0 for _ in range(total + 1)]

    for log in logs:
        log = log.split("-")
        start = decode_time(log[0])
        end = decode_time(log[1])

        cumul_data[start] += 1
        cumul_data[end] -= 1

    for i in range(1, total + 1):
        cumul_data[i] += cumul_data[i - 1]

    for i in range(1, total + 1):
        cumul_data[i] += cumul_data[i - 1]

    answer = 0
    result = cumul_data[adv - 1]  # !!!
    for i in range(0, total - adv):
        if result < cumul_data[i + adv] - cumul_data[i]:
            result = cumul_data[i + adv] - cumul_data[i]
            answer = i + 1

    return encode_time(answer)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]), "01:30:59")
print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]), "01:00:00")
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]), "00:00:00")
print(solution("00:00:10", "00:00:01", ["00:00:09-00:00:10"]))
