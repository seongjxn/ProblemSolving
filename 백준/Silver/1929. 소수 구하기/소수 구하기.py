N, M = map(int, input().split())
Li = [i for i in range(M + 1)]
Li[1] = 0

for i in range(2, int(M ** (1/2)) + 1) :
    if Li[i] == 0 :
        continue
    for j in range(i * i, M + 1, i) :
        Li[j] = 0

prime_numbers = [i for i in Li[N:M + 1] if Li[i]]
for p in prime_numbers :
    print(p)