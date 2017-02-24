def valid_parentheses(s):
    count = 0
    for c in s:
        count += 1 if c == '(' else -1 if c == ')' else 0
        if count < 0:
            return False
    return count == 0

