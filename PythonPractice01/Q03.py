def solution(input_str):
    answer = ""
    input_dic = {} 
    for i in input_str:
        if i in input_dic.keys():
            input_dic[i] += 1
        else:
            input_dic[i] = 1
    input_list = list(input_dic.keys())
    print(input_dic.keys())
    input_list.sort()

    for i in input_list:
        answer += i
        answer += str(input_dic[i])
    
    print(answer)

solution("agfdfdbgf")