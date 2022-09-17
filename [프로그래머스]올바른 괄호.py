# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
#
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
#
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# Code1 => 실패 코드
def solution(s):
    flag = True
    stack = []
    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if stack == []:
                flag = False
            else:
                stack.pop(0)
                flag = True
    if len(stack) >= 1:
        flag = False
    return flag

# Code2
def solution(s):
    flag = True
    stack = []
    for i in s:
        if i == "(":    # 만약 여는 괄호라면?
            stack.append("(")   # 스택에 여는 괄호를 추가
        else:           # 만약 닫는 괄호라면?
            if stack == []:     # 만약 빈 스택이라면?
                flag = False    # 올바른 괄호가 아니므로 False
                break
            else:               # 만약 들어있는 스택이라면?
                stack.pop()     # 마지막 괄호를 제거해준다.
                flag = True     # 올바른 괄호 한 쌍이 나오므로 True
    if stack != []:             # 끝까지 돌렸을때 만약 스택이 빈 상태가 아니라면? => 올바른 괄호가 아니라는 의미
        flag = False
    return flag

