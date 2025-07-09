def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    
    for b in babbling :
        for p in pron :
            b = b.replace(p, " ")
            if not b.strip() :
                answer += 1
                break
    return answer