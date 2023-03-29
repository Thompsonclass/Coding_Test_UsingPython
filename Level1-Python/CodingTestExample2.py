# 문제 설명 :
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 들어가기 앞서 생각하기 중복for문 사용 그리고, 튜플을 사용해 중복X, 뒤죽박죽 섞인건 sort()함수를 사용해서 정렬하기!!
def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if numbers[i] != numbers[k]:
                result.append(numbers[i] + numbers[k])
                result.sort()
    return list(set(result))

# 문제발생 : 해당 함수는 numbers 요소에 중복 요소가 있으면 오류가 발생합니다./ 정확성 : 22.2
# 해결방안 : if을 한 번 조정해보자

def solution(numbers):
    result =[]
    for i in range(len(numbers)):
        for k in range(len(numbers)):
            if i != k:
                result.append(numbers[i] + numbers[k])
                result.sort()
    return list(set(result))

# 문제발생 : 해당 함수도 오류 발생, 하지만 많이 개선/ 정확성 : 77.8
# 해결방안 : if문을 제거하고 for문의 인덱스 요소를 조절해서 해결할 거 같다고 판단.

def solution(numbers):
    result =[]
    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):
                result.append(numbers[i] + numbers[k])
                result.sort()
    return list(set(result))

# 문제 해석 : i는 고정적으로 인덱스 0부터 k의 요소를 +1해서 겹치지 않도록 하나하나 더하여 주면 해결

print("결과 : " + solution[2,1,3,4,1])
print("결과 : " + solution[5,2,0,7])
    