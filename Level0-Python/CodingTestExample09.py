# 문제 설명 
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
# 출력 예시 : my_string = "BCBdbe", letter = "B", result = "Cdbe" 

def solution(my_string, letter):
    list_res = []
    for i in my_string:
        if i != letter:
            list_res.append(i)
    return ''.join(list_res)

# 개선 사항_1 : "컴프리 헨션 형태"사용
def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])

# 설명 : 요소를 하나 하나 꺼내 조건을 걸고, 리스트 형태를 .join함수를 사용해 변환

# 출력
print("출력 : " + solution("CSGdfe", "C"))
print("출력 : " + solution("BCBdbe", "B"))
