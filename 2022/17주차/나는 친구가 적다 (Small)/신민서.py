first = input()
second = input()
new_one = ''

for f in first:
    if f.isalpha():
        new_one += f

if second in new_one:
    print(1)
else:
    print(0)

