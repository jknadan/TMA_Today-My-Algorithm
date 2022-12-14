# N, M = map(int, input().split())  # 정수형으로 값 입력 받기, 스페이스바로 값 연속으로 받기
#
# # 2차원 배열 생성(https://dailylifeofdeveloper.tistory.com/132)
# arr = []  # 원본 행렬
# arr2 = []  # 각 행렬의 가장 작은 수들 모음
#
# # 행렬 중 행 부분 생성
# for _ in range(N):
#     arr.append(_)
#     arr2.append(_)  # 이 부분은 그냥 리스트 생성
#
# # 입력과 동시에 열 부분 생성
# for i in range(N):
#     arr[i] = list(map(int, input().split()))
#     arr2[i] = min(arr[i])  # 각 행의 가장 작은 값들 저장
#
# print(max(arr2))  # arr2의 저장된 값 중 가장 큰 값 출력
# N, W을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    print(min_value)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력