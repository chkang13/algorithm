import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tasks = list(map(int, input().split()))

for task in tasks:
    if task == 1:
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    elif task == 2:
        for i in range(n):
            for j in range(m//2):
                arr[i][j], arr[i][m-j-1] = arr[i][m-j-1], arr[i][j]
    elif task == 3:
        # 새로운 배열 만들어서 기존배열 바꾸기
        temp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i][j] = arr[n-1-j][i]
        # 크기 바꾸기
        n,m = m, n
        arr = temp
        
    elif task == 4:
        temp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i][j] = arr[j][m-1-i]

        n,m = m, n
        arr = temp

    elif task == 5:
        temp = [[0]*m for _ in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                temp[i][j+m//2] = arr[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                temp[i+n//2][j] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                temp[i][j-m//2] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                temp[i-n//2][j] = arr[i][j]
        arr =temp

    else:
        temp = [[0]*m for _ in range(n)]
        for i in range(n//2):
            for j in range(m//2):
                temp[i+n//2][j] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2):
                temp[i][j+m//2] = arr[i][j]
        for i in range(n//2,n):
            for j in range(m//2,m):
                temp[i-n//2][j] = arr[i][j]
        for i in range(n//2):
            for j in range(m//2,m):
                temp[i][j-m//2] = arr[i][j]
        arr =temp

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()