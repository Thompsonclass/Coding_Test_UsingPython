# 문제 설명
# 정수 num1, num2가 매개변수로 주어질 때, 
# num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 < num1 ≤ 100
# 0 < num2 ≤ 100

# 입출력 예
# num1	num2	result
# 3	    2	    1
# 10	5	    0   

def solution(num1, num2):
    if 0 < num1 <= 100 and 0 < num2 <= 100: 
        return num1 % num2
    
    
# 출력
print("출력 : " + solution(13, 3))
print("출력 : " + solution(23, 2))