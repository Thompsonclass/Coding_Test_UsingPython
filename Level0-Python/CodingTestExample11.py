# 문제 설명 :
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 입출력 예
#   n	result
#   10	30
#   4	6

def solution(n):
    answer = 0
    for i in range(n + 1) :
        if (i % 2 == 0) :
            answer = answer + i 
    return answer

# 출력
print("출력 : " + solution(19))
print("출력 : " + solution(4))