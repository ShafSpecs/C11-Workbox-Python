open_brackets: list = ['(', '[', '{']
close_brackets: list = [')', ']', '}']


def check_brackets(string: str) -> bool:
  stack: list = []
  
  for i in range(0, len(string)):
    if close_brackets.count(string[i]) <= 0:
      stack.append(string[i])
    else:
      if close_brackets.index(string[i]) == open_brackets.index(stack[len(stack) - 1]):
        stack.pop()
    
  if len(stack) == 0:
    return True
  
  return False


print(input("Enter your bracket pattern: "))
