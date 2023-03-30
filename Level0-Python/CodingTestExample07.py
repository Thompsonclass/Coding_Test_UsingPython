# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
# 제한사항 : 1 ≤ num_list의 길이 ≤ 100, 0 ≤ num_list의 원소 ≤ 1,000
# 호출 결과 : num_list = [1, 2, 3, 4, 5], sum_result = [2, 3]

def solution(num_list):
    len1 = len(num_list)
    num1 = 0
    num2 = 0
    num_jac = []
    num_hol = []
    sum_result = []
    for x in num_list:
        if 1 <= len1 <= 100 and 0 <= x <= 1000:
            if x % 2 == 0:
                num_jac.append(x)
                num1 = len(num_jac) # 2
            elif x % 2 == 1:
                num_hol.append(x)
                num2 = len(num_hol) # 3       
    sum_result.append(num1)
    sum_result.append(num2)
    return sum_result

#개선사항_1 : 
def solution(num_list) :
    answer = [0,0]
    for i in num_list:
        answer[i%2] = answer[i%2] + 1
    return answer
    
# 설명 : answer배열의 인덱스를 응용하여 문제 해석

# 출력
print("출력 : " + solution([1, 2, 3, 4, 5]))
print("출력 : " + solution([1, 2, 3, 4, 5, 7, 8, 8]))