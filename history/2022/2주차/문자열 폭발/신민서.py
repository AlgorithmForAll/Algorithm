inp = input()
dele = input()

stack = []
chk = []


for i in inp:
    stack.append(i)
    if i == dele[-1] and ''.join(stack[-len(dele):]) == dele: #시간효율
        del stack[-len(dele):] #시간효율

answer = ''.join(stack) #시간효율

if answer == "":
    print("FRULA")
else:
    print(answer)