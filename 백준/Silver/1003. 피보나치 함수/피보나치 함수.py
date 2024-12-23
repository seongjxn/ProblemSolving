import sys ; input = sys.stdin.readline

def fibonacci(n : int) :
    if DP_Li[n] is not None :
        return DP_Li[n]
    
    result = [0, 0]
    
    if (n == 0) :
        result = [1, 0]
    elif (n == 1) :
        result = [0, 1]
    else :
        r1 = fibonacci(n-1) 
        r2 = fibonacci(n-2)
        result = [r1[0]+r2[0], r1[1]+r2[1]]
    
    DP_Li[n] = result
    return result
    

T = int(input().rstrip())
DP_Li = [None for _ in range(40 + 1)]

for _ in range(T) :
    result = fibonacci(int(input().rstrip()))
    print(result[0], result[1])
