# 문제 설명 : 
# 정수 n이 매개변수로 주어질 때, n이하의 홀수가 오름차순을 담긴배열을 return하도록 solution함수를 완성하시오.
# 제한 사항 : 1 <= n <= 100
def solution(n):
    answer = []
    if 1<=n<=100:
        for k in range(1, n+1):
            if k % 2 == 1:
                answer.append(k)    
        return answer

# 출력
print("출력 : " + solution(10))
print("출력 : " + solution(30))
