def solution(arr):
    answer = []
    for i in arr :
        if i >= 50 and not i % 2 :
            i /= 2
        elif i <= 50 and i % 2 :
            i *= 2
        answer.append(i)
    return answer