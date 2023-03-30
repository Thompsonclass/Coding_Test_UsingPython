# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    for k in numbers:
        answer.append(k * 2)            
    return answer

#출력
solution([1,2,3,4,5,6])


#개선 사항_1 : "컴프리 헨션 형태"(Comprehensive form)
def solution(numbers):
   return [num*2 for num in numbers]

#개선 사항_2 : "람다식 형태"(lambda form)
def solution(numbers):
   return list(map(lambda num : num * 3, numbers))

#출력
print("출력 : " + solution([1,2,3,4,5,6]))
print("출력 : " + solution([1,2,3]))
