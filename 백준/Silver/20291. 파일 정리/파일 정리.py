from collections import defaultdict
N = int(input())
save = defaultdict(int)

while N>0:
    name,ext = input().split('.')
    save[ext] += 1
    N -= 1

exts = list(save.keys())
exts.sort()

for ext in exts:
    print(ext, save[ext])