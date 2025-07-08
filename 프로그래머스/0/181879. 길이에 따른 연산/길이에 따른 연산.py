def solution(num_list):
    if len(num_list) > 10 :
        answer = sum(num_list)
    else :
        for num in num_list:
            try:
                answer *= num
            except:
                answer = num
    
    return answer