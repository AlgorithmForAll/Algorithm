S = list(filter(str.isalpha, input()))
K = input()

S = ''.join(S)
if K in S:
    print(1)
else:
    print(0)