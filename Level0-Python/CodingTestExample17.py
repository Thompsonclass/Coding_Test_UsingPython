# 문제 설명
# 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 1,000,000

# str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.

# 입출력 예

# 입력
# HelloWorld!

# 출력
# HelloWorld!

str = input().strip()
#입력 함수, 양끝 공백 제거 함수
str_len = len(str)
#str입력 변수 길이
if 1<=str_len<=1000000:
    #제한 사항
    print(str)
    #출력