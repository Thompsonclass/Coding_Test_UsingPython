# 문자열 돌리기

# 문제 설명
# 문자열 str이 주어집니다.
# 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 10

# === 입출력 예 === 

# 입력
# abcde

# 출력
# a
# b
# c
# d
# e

str = input().strip()
#사용자 입력 함수, 양쪽 공백 제거함수
def solution(str):
    str_len=len(str)
    str_result = ''
    if not 1<=str_len<=10:
        #제한사항
        return "false"
    for i in str:
        str_result += i + '\n'
        # \n으로 인해 90도로 출력
    return str_result
    #return str_result.rstrip('\n')가 더욱 확실한 답
print(solution(str))
