# 덧셈식 출력하기
# 문제 설명
# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

# 형태 : a + b = c

# 제한사항
# 1 ≤ a, b ≤ 100

# === 입출력 예 === 

# 입력
# 4 5

# 출력
# 4 + 5 = 9

def solution(a, b):
    if not (1 <= a <= 100) or not (1 <= b <= 100):
        #제한사항
        return "false"
    result = a + b
    print(f'{a} + {b} = {result}')
    #템플릿 문자 이용(타입 : 문자열)

a, b = map(int, input().strip().split(' '))
#사용자입력 함수, 양쪽 공백제거 함수, 공백을 기준으로 리스트 형태로 만들어주는 함수
solution(a, b)