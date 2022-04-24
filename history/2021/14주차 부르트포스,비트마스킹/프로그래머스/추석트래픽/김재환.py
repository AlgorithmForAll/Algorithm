"""
각 end 구간을 기준으로 범위를 비교하면
개수가 2000개 이므로 N*2*(시작이 포함되는 경우까지만)
"""


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration):
    n_time = duration[:-1]
    int_duration = int(float(n_time) * 1000)  # 1000ms가 최대
    return get_time(time) - int(int_duration) + 1


def solution(lines):
    print(lines)
    times = []
    for t in range(len(lines)):
        tline = lines[t]
        date, time, sec = tline.split()
        print(date, time, sec)
        end = get_time(time)
        start = get_start_time(time, sec)
        times.append([start, end])
    # 구간 비교 시작
    big = 0
    for t in range(len(lines)):
        # 1분 구간 구하기
        count = 0
        start, end = times[t]
        for n in range(t, len(lines)):
            start = times[n][0]
            if end > start - 1000:
                count += 1
        big = max(big, count)
    print(big)
    return big


solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
])
