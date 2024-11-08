# BOJ 9012 : 괄호
# https://www.acmicpc.net/problem/9012


import sys ; input = sys.stdin.readline

def func() :
    PS = input().rstrip()
    valid = []

    for p in PS :
        if p is "(" :
            valid.append('(')
            continue
        if p is ")" :
            try:
                valid.pop()
            except :
                return "NO"

    return "YES" if not valid else "NO"

count = int(input().rstrip())
result = [func() for _ in range(count)]

for res in result :
    print(res)