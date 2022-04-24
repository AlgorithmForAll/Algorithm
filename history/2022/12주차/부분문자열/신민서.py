def kmp(n, m, pi):
    idx = 0
    for i in range(len(n)):
        while idx > 0 and m[idx] != n[i]:
            idx = pi[idx - 1]
        if m[idx] == n[i]:
            idx += 1
        if idx == len(m):
            return 1
    return 0


def constructpi(m, pi):
    idx = 0
    for i in range(1, len(m)):
        while idx > 0 and m[i] != m[idx]:
            idx = pi[idx-1]
        if m[i] == m[idx]:
            idx += 1
            pi[i] = idx
    return pi


n = input()
m = input()
pi = [0] * len(m)
constructpi(m, pi)
print(kmp(n, m, pi))
