# 문제 설명 :
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

# 입출력 예 :
# numbers	                    result
# [1, 2, 3, 4, 5]	            [2, 4, 6, 8, 10]
# [1, 2, 100, -99, 1, 2, 3]	    [2, 4, 200, -198, 2, 4, 6]

def solution(numbers):
    answer = []
    for k in numbers:
        answer.append(k * 2)            
    return answer

# 개선사항_1 : "컴프리 헨션 형태"사용
def solution(numbers):
    return [x *2 for x in numbers]

# 출력
print("출력 : " + solution([1,2,3,4,5]))
print("출력 : " + solution([1, 2, 100, -99, 1, 2, 3]))