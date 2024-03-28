from collections import defaultdict
log = defaultdict(str)
office = []
n = int(input())

for _ in range(n):
    name, come = input().split()
    log[name] = come

for key in log.keys():
    if log[key] == 'enter':
        office.append(key)

office.sort(reverse=True)

for i in office: 
    print(i)