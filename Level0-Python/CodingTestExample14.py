# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 10,000
# 2 ≤ numbers의 길이 ≤ 100

# 입출력 예
# numbers	            result
# [1, 2, 3, 4, 5]	    20
# [0, 31, 24, 10, 1, 9]	744

def solution(numbers):
    numbers_len = len(numbers)
    if not 2 <= numbers_len <= 100: 
        return False
    for number in numbers:
        if not 0 <= number <= 10000:
            return False
    # 여기 까지는 제한 사항에 대한 판단
    max_result = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            product = numbers[i] * numbers[j]
            if product > max_result:
                max_result = product
    return max_result
    # 중첩 for문을 이용해 각 요소를 전부 곱하고 높은 수를 반환