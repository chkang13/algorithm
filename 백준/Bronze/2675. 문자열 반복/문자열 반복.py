T = int(input())
P = [""]*T
for i in range(T):
    R,S = input().split()
    for word in S:
        P[i] += word*int(R)

for p in P:
    print(p)