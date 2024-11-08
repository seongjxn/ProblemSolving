# BOJ 1343 : 폴리오미노
# https://www.acmicpc.net/problem/1343


import sys ; input = sys.stdin.readline

def solution(S : str):
    S = S.replace('XXXX', 'AAAA')
    S = S.replace('XX', 'BB')

    if S.count('X') : return -1
    else: return S

if __name__ == '__main__' :
    print(solution(input()))