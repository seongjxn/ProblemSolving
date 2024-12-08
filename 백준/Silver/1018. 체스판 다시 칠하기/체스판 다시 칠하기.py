import sys ; input = sys.stdin.readline

N, M = map(int, input().split())
Li = [list(input()) for _ in range(N)]
result = 50*50

for row in range(N - 7) :
    for col in range(M - 7) :
        changeCnt = 50*50
        
        for color in range(2) :
            change = 0
            
            for r in range(row, row + 8) :
                for c in range(col, col + 8) :
                    if (not r % 2 and not c % 2) or (r % 2 and c % 2) :
                        if (not color and Li[r][c] != 'W') or (color and Li[r][c] != 'B') :
                            change += 1
                    else :
                        if (not color and Li[r][c] != 'B') or (color and Li[r][c] != 'W') :
                            change += 1
            
            changeCnt = min(changeCnt, change)
        result = min(result, changeCnt)
    
print(result)