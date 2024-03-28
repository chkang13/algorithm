N = int(input())
score = list(map(int, input().split()))
max_score = max(score)

for i, num in enumerate(score):
    score[i] = num/max_score * 100

print(sum(score)/len(score))