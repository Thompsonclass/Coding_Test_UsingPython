# 문자열 붙여서 출력하기

# 문제 설명
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str1, str2의 길이 ≤ 10

# === 입출력 예 ===
# 입력
# apple pen

# 출력
# applepen

# 입력
# Hello World!

# 출력
# HelloWorld!

def solution(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if not 1<=str1_len<=10 or not 1<=str2_len<=10:
        #제한 사항
        return "false"
    result = str1 + str2
    print(result)
str1, str2 = input().strip().split()
#사용자 입력 함수, 양쪽 공백 제거함수, 리스트 형태로 반환 함수
solution(str1, str2)