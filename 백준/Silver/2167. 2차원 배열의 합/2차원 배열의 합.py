# BOJ 2167 : 2차원 배열의 합
# https://www.acmicpc.net/problem/2167


import sys ; input = sys.stdin.readline

def solution(Li : list) :
    i, j, x, y = map(int, input().rstrip().split())
    return Li[x][y] - (Li[x][j - 1] + Li[i - 1][y]) + Li[i - 1][j - 1]
    

if __name__ == '__main__' :
    N, M = map(int, input().rstrip().split())
    Li = [list(map(int, input().rstrip().split())) for _ in range(N)]
    Li_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            Li_sum[i][j] = Li_sum[i][j - 1] + Li_sum[i - 1][j] - Li_sum[i - 1][j - 1] + Li[i - 1][j - 1]

    for _ in range(int(input().rstrip())) :
        print(solution(Li_sum))
 