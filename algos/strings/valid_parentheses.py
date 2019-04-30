# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


def valid_parentheses(s):
    dic = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for c in s:
        if c in dic.keys():
            stack.append(c)
        else:
            if not stack or dic[stack[-1]] != c:
                return False
            stack.pop()
    return not stack
