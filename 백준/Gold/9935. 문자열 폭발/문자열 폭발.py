import sys
input = sys.stdin.readline

sentence = input().rstrip()
bomb = input().rstrip()

stack = []
for i in range(len(sentence)):
    stack += sentence[i]
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else: print('FRULA')