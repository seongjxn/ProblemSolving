# BOJ 10845 : 큐
# https://www.acmicpc.net/problem/10845


import sys ; input = sys.stdin.readline

def func(Q: list) :
    oper = input().rstrip()
    
    if oper.startswith('push') :
        Q.append(int(oper.split()[-1]))
    elif oper.startswith('pop') :
        try: print(Q.pop(0))
        except: print(-1)
    elif oper.startswith('size') :
        print(len(Q))
    elif oper.startswith('empty') :
        if Q : print(0)
        else : print(1)
    elif oper.startswith('front') :
        if Q : print(Q[0])
        else : print(-1)
    elif oper.startswith('back') :
        if Q : print(Q[-1])
        else : print(-1)
        

QUEUE = []

for _ in range(int(input().rstrip())) :
    func(QUEUE)