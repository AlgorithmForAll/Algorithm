tmp = list(input())
check = input()
_tmp = ""
for t in tmp:
    if 'a' <= t <= 'z' or 'A' <= t <= 'Z':
        _tmp += t
if check in _tmp:
    print(1)
else:
    print(0)
