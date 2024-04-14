import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def change(t):
    if t == s:
        print(1)
        exit()
    
    if len(t) == 0:
        return 
    
    if t[-1] == 'A': # 마지막이 A면 1번 연산을 한 것
        change(t[:-1]) # A를 제거한 값
    if t[0] == 'B': # 처음이 B이면 2번 연산을 한 것
        change(t[1:][::-1]) # 뒤집은 후 B 제거

change(t)

print(0)