s = "(())())"

def isValid(string):
    stack, match = [], {')': '('}
    for ch in string:
        #1 ")" 나온 경우
        if ch in match:

            # 1-1) stack and (stack.pop() --> ")" 나온 경우) if 안에 들어 감
            # 주의! 조건문 내에서 pop이 수행되면서 다음 수행에도 적용이 됨
            if not (stack and (stack.pop() == match[ch])):
                return False
        #2 "(" 나온 경우
        else:
            stack.append(ch)
    return not stack

print(isValid(s))
