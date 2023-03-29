# 문제 설명 : 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
# 입출력 예 : num = 3, return = "Odd" / num = 4, return = "Even"

def solution_1(num):
    if num % 2 == 0:
        return "Even"
    elif num % 2 == 1:
        return "Odd"

# 개선 사항_1  
def solution_2(num_1):
    if num_1 % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# 개선 사항_2
def solution_3(num_2):
    if num_2 % 2:
        return "Odd"
    return "Even"
# 1은 True, 0은 False로 처리
# 문제 해석 : 짝수인지 홀수인지 여부는 2의 정수로 나누었을 때 0이냐 1이냐 둘 중 하나이기에 다음과 같이 함수를 만들 수 있습니다.

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("결과 : " + solution_3(3))
print("결과 : " + solution_3(2))