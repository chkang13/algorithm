from collections import Counter
import sys
input = sys.stdin.readline

name = input().rstrip()
count = Counter(name)

center = ''
odd = 0
for alpha in count:
    if count[alpha] % 2 == 1:
        odd += 1
        center = alpha
        if odd == 2:
            print("I'm Sorry Hansoo")
            exit()

result = ''
keys = sorted(count.keys())
for key in keys:
        result += key * (count[key] // 2)
print(result + center + result[::-1])