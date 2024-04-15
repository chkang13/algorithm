import sys
input = sys.stdin.readline

N = int(input())
R = int(input())
num = list(map(int, input().split()))

photo = dict()

for i in range(R):
    if num[i] not in photo: # 새 후보 추천

        if len(photo) >= N: # 비어있는 사진틀이 없으면
            del_photo = sorted(photo.items(), key = lambda x : (x[1][1] , x[1][0]) )
            del_key = del_photo[0][0] # 추천 횟수가 가장 적고 오래된 사진
            del(photo[del_key])
            photo[num[i]] = [i, 1]

        else: # 비어있는 사진틀이 있으면
            photo[num[i]] = [i, 1] # (게시 시간, 추천 수)

    else: # 기존 후보 추천
        photo[num[i]][1] += 1 # 추천 수 증가 

students = sorted(photo.keys())
print(*students)