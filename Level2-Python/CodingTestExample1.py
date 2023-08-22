#올바른 괄호

#문제 설명
#괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

#"()()" 또는 "(())()" 는 올바른 괄호입니다.
#")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
#'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):
    stack = []  # 스택으로 사용할 리스트

    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:  # 스택이 비어있는데 닫힌 괄호가 나온 경우
                return False
            stack.pop()  # 열린 괄호와 닫힌 괄호가 매칭되므로 스택에서 제거
        else:
            return False  # 괄호 이외의 문자가 들어있는 경우

    return len(stack) == 0  # 스택이 비어있으면 모든 괄호가 올바름 확인

#제한사항
#문자열 s의 길이 : 100,000 이하의 자연수
#문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

#입출력 예
#s	answer
#"()()"	true
#"(())()"	true
#")()("	false
#"(()("	false