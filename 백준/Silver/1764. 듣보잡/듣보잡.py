import sys
input = sys.stdin.readline

hear = {}
hear_see = []

n,m = map(int, input().rstrip().split())

for i in range(n):
    name = input().rstrip()
    hear[name] = True

for i in range(m):
    name = input().rstrip()
    if name in hear:
        hear_see.append(name)

hear_see.sort()
print(len(hear_see))
print(*hear_see, sep="\n")
