s = "()[]{}"


def valid_paren(string1):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in string1:
       if char in mapping.values():      # (
           stack.append(char)            # [(]
       elif char in mapping.keys():    # )
           if not stack or mapping[char] !=stack.pop():      #), ], }!= (,[,{
               print(stack.pop())
               return False
    return not stack
       
    
print(valid_paren(s))


