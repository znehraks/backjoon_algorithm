# name = "정민"
# age = 26
# school = "MJU"
# job = "student"
# dream = "재밌게 돈많이벌며 행복하게 사는 것"
# print("안녕하슈 나는",name,"이라고합니다. 저는", age,"살이고, 학교는",school,"이며 직업은",job,"이고 꿈은",dream,"입니다")

def solution(input_str):
    answer = ""
    for i in range(10):
        if str(i) in input_str:
            pass
        else:
            answer += str(i)

    return answer
print(solution("012345678"))
# str = [1,2,3,4]
# str.pop(1)
# print(str)