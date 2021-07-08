def solution(input_str):
    answer = ""
    numbers = "0123456789"
    for i in input_str:
        if str(i) in numbers:
            continue
        else: 
            answer += str(i)
    return answer

print(solution("H123H123L1L1O"))
print(solution("A0123P3132P2395343L494E44"))