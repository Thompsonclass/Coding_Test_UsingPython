# 문제 설명
# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 10
# 1 ≤ n ≤ 5

# 입출력 예

# 입력 #1
# string 5

# 출력 #1
# stringstringstringstringstring

str, n = input().strip().split() # str, n = ['string', '5']를 의미합니다.

def add(str, n):
    result = ""
    str_len = len(str)
    if not 1 <= str_len <= 10:
        return False
    if not 1 <= n <= 5:
        return False
    for i in range(n):
        result += str
    return result
print(add(str, int(n)))

# 부족한 점
# 1) strip(), split() 함수에 대한 이해
# 1-1) strip()
# 시작과 끝에 있는 공백을 제거해줍니다. 그리고 strip('aa')를 통해 시작과 끝에 있는 'aa'문자를 제거합니다. 그래서 붙이는 편이 좋습니다.
# 1-2) split()
# 해당 함수안에 매개변수가 없으면, 공백을 기준으로 문자를 나누어서, 배열 형태로 쪼개서 만듭니다.
# ex) str = 'strings 5'의 형태라면 ['strings', '5']의 형태로 바꾸어줍니다.
# 2) 문자열을 합치는 방법에 대한 이해