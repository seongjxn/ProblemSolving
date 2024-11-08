# BOJ 9375 : 패션왕 신해빈
# https://www.acmicpc.net/problem/9375


import sys ; input = sys.stdin.readline

def solution(N : int) -> int :
    wear_dict = {}

    for _ in range(N) :
        wear, type = map(str, input().rstrip().split())
        try:    wear_dict[type] += 1
        except: wear_dict[type] = 1

    result = 1
    for value in wear_dict.values() :
        result *= value + 1
    return result - 1

if __name__ == '__main__' :
    for _ in range(int(input().rstrip())) :
        print(solution(int(input().rstrip())))