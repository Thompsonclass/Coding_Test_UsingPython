# 문제 설명 : String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
# 입출력 예 :seoul = ["Jane", "Kim"], return = "김서방은 1에 있다"

def solution(seoul):
    answer = ''
    for k in range(len(seoul)):
        if seoul[k] == "Kim":
            answer = k
    return "김서방은 " + str(answer) + "에 있다"

# 출력
print("출력 : " + solution(["Jane", "Kim"]))
print("출력 : " + solution(["Kim", "Jane"]))