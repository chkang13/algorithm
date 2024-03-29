import sys
input = sys.stdin.readline

user = {}

N = int(input())
gom = 0
while N>0:
    nick = input().rstrip()
    if nick == 'ENTER':
        gom += len(user)
        user.clear() # del user는 딕셔너리 자체가 제거
    
    if nick != 'ENTER' and nick not in user:
        user[nick] = 1
    
    N -= 1

gom += len(user)
print (gom)