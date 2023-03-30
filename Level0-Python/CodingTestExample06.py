# 문제 설명
# 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
# 제한 사항 : 1 <= array 길이 <= 100, 0 <= array 원소 <= 1,000, arraty에 중복된 숫자는 없습니다.

def solution(array):
    answer = []
    answer.append(max(array))
    for k in range(len(array)):
        if answer[0] == array[k]:
             answer.append(k)
    return answer

#개선 사항_1 : "컴프리 헨션 형태"(Comprehensive form)
def solution(array):
    answer = []
    array_len = len(array)
    answer.append(max(array))
    [answer.append(k) for k in range(len(array)) if answer[0] == array[k] if 0 <= array[k] <= 1000 if 1 <= array_len <= 100]
    return answer

#개선 사항_2 : 제한 사항 제외 코드
def solution(array):
    answer = []
    array_len = len(array)
    answer.append(max(array))
    [answer.append(k) for k in range(len(array)) if answer[0] == array[k]]
    return answer


# 출력
print("출력 : " + solution([1, 8, 3]))
print("출력 : " + solution([1, 9]))