# BOJ 1920 : 수 찾기
# https://www.acmicpc.net/problem/1920


import sys ; input = sys.stdin.readline
from typing import List

def solution(Li_1 : set, Li_2 : List[int]) :
    for num in Li_2 :
        if num in Li_1 : print(1)
        else :           print(0)

        

if __name__ == '__main__' :
    _ = input()
    Li_1 = set(list(map(int, input().rstrip().split())))
    _ = input()
    Li_2 = list(map(int, input().rstrip().split()))

    solution(Li_1, Li_2)
