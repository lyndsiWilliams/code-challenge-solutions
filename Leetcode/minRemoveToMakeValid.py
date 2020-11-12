def minRemoveToMakeValid(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            if len(stack) and 


minRemoveToMakeValid("a)b(c)d")