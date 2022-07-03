bracket = input()
stack = []

check = 1
result = 0

for i in range(len(bracket)):
  if bracket[i] == '(':
    check *= 2
    stack.append(bracket[i])
  elif bracket[i] == '[':
    check *= 3
    stack.append(bracket[i])

  elif bracket[i] == ')':
    if not stack or stack[-1] == '[':
      result = 0
      break
  
    if bracket[i-1] == '(':
      result += check
      
    check //= 2
    stack.pop()
  
  else:
    if not stack or stack[-1] == '(':
      result = 0
      break
  
    if bracket[i-1] == '[':
      result += check
      
    check //= 3
    stack.pop()

if stack:
  result = 0
  
print(result)