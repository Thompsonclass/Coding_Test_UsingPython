#정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
#제한사항 : 1 ≤ n ≤ 100
#결과 출력 : n = 10, result = [1, 3, 5, 7, 9]

def solution(n):
    answer = []
    if 1<=n<=100:
        for k in range(1, n+1):
            if k % 2 == 1:
                answer.append(k)    
        return answer
    
#개선사항_1 : "컴프리 헨션 형태"사용
def solution(n):
    answer = []
    [answer.append(k) for k in range(1, n+1) if 1<=n<=100 if k % 2 == 1]
    return answer

#출력
print("출력 : " + solution(7))
print("출력 : " + solution(8))

