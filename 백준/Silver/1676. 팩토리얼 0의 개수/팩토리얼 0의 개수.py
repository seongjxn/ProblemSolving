N = int(input())
result = 1
count = 0

for i in range(N, 0, -1) :
    result *= i

for j in str(result)[::-1] :
    if j != '0' : break
    count += 1

print(count)