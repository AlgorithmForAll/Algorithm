
def timeToSec(time):
    min, sec = time.split(":")
    final = int(sec)
    final += 60*int(min)
    return final


def secToTime(sec):
    min = sec//60
    sec = sec % 60
    return str(min).zfill(2) + ":"+str(sec).zfill(2)


N = int(input())
team = [0, 0, 0]
final = [0, 0, 0]
pastTime = 0
for n in range(N):
    t, time = input().split()
    t = int(t)

    if team[1] > team[2]:
        final[1] += timeToSec(time) - timeToSec(pastTime)

    elif team[1] < team[2]:
        final[2] += timeToSec(time) - timeToSec(pastTime)

    team[t] += 1
    pastTime = time


if team[1] > team[2]:
    final[1] += timeToSec("48:00") - timeToSec(pastTime)

elif team[1] < team[2]:
    final[2] += timeToSec("48:00") - timeToSec(pastTime)

print(secToTime(final[1]))
print(secToTime(final[2]))
