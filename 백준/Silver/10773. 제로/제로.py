import sys ; input = sys.stdin.readline

K = int(input().rstrip())

numbers = []

for _ in range(K) :
    num = int(input().rstrip())
    
    if not num :
        numbers.pop(-1)
    else :
        numbers.append(num)
        
print(sum(numbers))