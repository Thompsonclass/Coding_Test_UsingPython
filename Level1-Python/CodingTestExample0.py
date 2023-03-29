#문제 설명 : 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요. 
#출력 예시 : a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def solution(a, b):
    if a < b :
        return (a+1)+a+b
    if a > b :
        return (a-1)+a+b
    if a == b :
        return a

#당장의 출력예시는 해결되지만, 장기간 사용을 보았을때 정확성, 효율성이 떨어짐. ex)1부터 10까지의 합을 구하시오.

#개선사항_1 : sum, list, range 함수를 복합적 사용.
def solution(a, b):
    if a < b:
        return sum(list(range(a, b+1)))
    else : 
        return sum(list(range(b, a+1)))

#개선사항_2 : 더욱 최소화
def solution(a, b):
    return sum(list(range(min(a, b), max(a, b) + 1)))