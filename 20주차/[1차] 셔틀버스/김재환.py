def minuteToTime(time):
    h = time // 60
    m = time % 60
    time = str(h).zfill(2) + ':' + str(m).zfill(2)
    return time


def timeToMinute(time):
    h, m = time.split(':')
    minute = int(h)*60+int(m)
    return minute


def solution(n, t, m, timetable):
    answer = ''
    timetable = sorted(timetable)
    result = []
    index = 0
    count = 0
    for i in range(n):
        busMinute = timeToMinute("09:00") + t*i

        # 가장 뒤의 시간을 구한다.
        while index < len(timetable) and count < m:
            if busMinute >= timeToMinute(timetable[index]):
                count += 1
                index += 1
            else:
                break
        if count < m:  # 최고 시간을 사용가능
            result.append(minuteToTime(busMinute))
        elif count == m:  # 마지막 시간보다 작아야함
            result.append(minuteToTime(timeToMinute(timetable[index-1]) - 1))
        count = 0
    return result[-1]
