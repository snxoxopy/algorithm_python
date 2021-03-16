from collections import deque

balanced_parentheses_string = "()))((()"

# 올바른 괄호 문자열인지 어떻게 알 수 있을까?

def is_correct_parenthesis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def seperate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u,v

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return  reversed_string

def change_to_correct_parenthesis(string):
    #1. 입력이 빈 문자열인 경우 빈 문자열을 반환
    if string == "":
        return ""

    #2. 문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리한다.
    #단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
    #v는 빈 문자열이 될 수 있다.
    # ( ) 개수가 같아야한다.
    u, v = seperate_to_u_v(string)

    #3. 문자열 u가 "올바른 괄호 문자열"이라면 v에 대해 1단계부터 다시 수행
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)

    #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행한다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)
    #return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!