# TODO : 단순하게 푼 문제
# N, K = map(int, input().split())  # 정수형으로 값 입력 받기, 스페이스바로 값 연속으로 받기
# count = 0
#
# while N != 1:
#     if N % K == 0:
#         N = N / K
#         count += 1
#     else:
#         N -= 1
#         count += 1
#
# print(count)

# 입력값 : 100000 87654
# 출력값 : 12347

# TODO : 개선 방안

N, K = map(int, input().split())  # 정수형으로 값 입력 받기, 스페이스바로 값 연속으로 받기
count = 0

while N != 1:
    count += (N % K) + 1
    N = int(N / K)  # 몫만 저장하기 ( // 연산자로 대체 가능)

print(count)
