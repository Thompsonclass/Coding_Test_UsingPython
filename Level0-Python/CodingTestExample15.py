# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때,
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을
# return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# my_string은 영어 대문자와 소문자로만 구성되어 있습니다.

# 입출력 예
# my_string	    result
# "cccCCC"	    "CCCccc"
# "abCdEfghIJ"	"ABcDeFGHij"

def solution(my_string):
    my_string_len = len(my_string)
    if not 1 <= my_string_len <= 1000:
        return 'false'
    # 제한 사항 적용
    result_str = ''
    for i in my_string:
        if i.isupper():
            result_str+=i.lower()
        if i.islower():
            result_str+=i.upper()
    return result_str
    # 대문자를 소문자로, 소문자를 대문자로 변환

# 부족한 점
# 1) isupper(), islower() 내장 함수 사용법
# 2) 문자열은 수정이 불가능
# 3) 새로 생성한 문자열을 대상으로 문자를 추가 시키는 방법