N, M, K = map(int, input().split())  # 정수형으로 값 입력 받기, 스페이스바로 값 연속으로 받기
A = 0  # 정답이 될 변수
count = 0  # 연속 연산 횟수
# 각 변수들의 범위
if (2 >= N) and (N >= 1000):
    print('N의 범위가 잘못되었습니다.')

if (M <= 1) and (M >= 10000):
    print('M의 범위가 잘못되었습니다.')

if (K <= 2) and (K >= 10000):
    print('K의 범위가 잘못되었습니다.')

N_list = list(map(int, input().split()))  # map 함수를 쓰면 for 문을 안써도 한번에 배열 입력이 가능하대

# 연산 과정
for i in range(M - 1):  # M-1번 연산
    A += max(N_list)  # 가장 큰 수를 우선적으로 연산
    count += 1  # 연산 후 횟수 +1
    if count == K:  # 연속 연산이 K번과 동일해지면
        temp = max(N_list)  # 잠시 가장 큰 수를 저장하고
        N_list.remove(temp)  # 뺀다 (remove() : "입력한 값을 검색해서, 첫 번째 검색 결과를 삭제")
        A += max(N_list)  # 그리고 그 다음으로 큰 수 하나를 연산
        count = 0  # 연속 연산 초기화
        N_list.append(temp)  # 다시 원래 가장 큰수 리스트에 추가

print(A)
