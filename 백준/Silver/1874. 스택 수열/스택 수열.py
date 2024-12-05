import sys ; input = sys.stdin.readline

n = int(input().rstrip())
Li = [int(input().rstrip()) for _ in range(n)]

St = []
res = []

St_num = 1
for N in Li:    
    while True:
        if St :
            if St[-1] == N :
                tmp = St.pop()
                res.append('-')
                break
                
            elif St[-1] < N :
                St.append(St_num)
                res.append('+')
                St_num += 1
                
            else :
                print('NO')
                exit()
        else :
            St.append(St_num)
            res.append('+')
            St_num += 1

for r in res :
    print(r)