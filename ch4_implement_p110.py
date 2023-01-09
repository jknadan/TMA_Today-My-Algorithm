N = int(input())
x = 1
y = 1

# 2차원 N x N 행렬 선언
arr = [[0 for j in range(N)] for i in range(N)]

# A가 이동할 여행 계획 리스트
i = 0

while True:
    arr2 = list(map(str, input().split()))
    if [arr2] == '\n':
        break
    i += 1

for i in arr2:
    if x <= 0 or x > N or y <= 0 or y > N:
        x = x
        y = y
    else:
        if arr[i] == 'R':
            if y <= 0 or y > N:
                y = y
            y += 1
        elif arr[i] == 'L':
            if y <= 0 or y > N:
                y = y
            y -= 1
        elif arr[i] == 'U':
            if x <= 0 or x > N:
                x = x
            x -= 1
        elif arr[i] == 'D':
            if x <= 0 or x > N:
                x = x
            x += 1

print(x,y)