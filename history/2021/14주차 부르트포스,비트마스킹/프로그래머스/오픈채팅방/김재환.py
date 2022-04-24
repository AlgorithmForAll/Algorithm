def solution(record):
    result = []
    ment = ['님이 들어왔습니다.', '', "님이 나갔습니다."]
    users = {}
    for re in record:
        tmp = re.split()
        cmd = tmp[0]
        uid = tmp[1]
        if cmd == "Enter":
            name = tmp[2]
            users[uid] = name
            result.append([uid, 0])
        elif cmd == "Change":
            name = tmp[2]
            users[uid] = name
        else:  # leave
            result.append([uid, 2])
    for i in range(len(result)):
        uid, cmd = result[i]
        result[i] = "".join(users[uid])+ment[cmd]

    return result
