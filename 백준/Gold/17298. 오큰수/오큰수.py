import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

stack = [0]
nge = [-1] * n

for i in range(n):
    while stack:
        if nums[stack[-1]] < nums[i]:
            nge[stack.pop()] = nums[i]
        else : break
    stack.append(i)

print(*nge)  
