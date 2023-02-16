# N, L = map(int, input().split())  # 정수형으로 값 입력 받기, 스페이스바로 값 연속으로 받기
# array = list(map(int, input().split()))

Ti, Pi = [3, 5, 1, 1, 2, 4, 2], [10, 20, 10, 20, 15, 40, 200]


def solution(start, temp):
    ret = 0
    global Ti, Pi

    for i in range(start, len(Ti), 1):
        print(i)
        if Ti[i] + start > len(Ti):
            continue
        temp += Pi[i]
        print(temp)
        print(Ti[i]+start)
        solution(Ti[i] + start, temp)

        if ret < temp:
            ret = temp

    return ret


print(solution(0, 0))
