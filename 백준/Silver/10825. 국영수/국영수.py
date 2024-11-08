# BOJ 10825 : 국영수
# https://www.acmicpc.net/problem/10825


import sys ; input = sys.stdin.readline

N = int(input())
stu_list = []
for _ in range(N) :
    name, kor, eng, math = map(str, input().split())
    stu_list.append([name, int(kor), int(eng), int(math)])

stu_list.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N) :
    print(stu_list[i][0])