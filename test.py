# 문자열 출력
print('Hello World!')

# 변수 설정

a = 2
b = 'hello'

print(a, b)  # 2 hello

# 변수형

a = 1
b = 3
c = 2.4

print(b ** b)  # b^b : b의 b제곱
print(c % b)  # 2.4

# 문자열

x = '안녕하세요'
y = '반갑습니다'

print(x, y)  # 안녕하세요 반갑습니다
print('안녕하세요' + '반갑습니다')  # 안녕하세요반갑습니다

z = '4'  # 문자 4
print(type(z))  # 결과: <class 'str'>
print(type(int(z)))  # 숫자 4로 변경 # 결과: <class 'int'>

# boolean

q = True
w = False

print(q, w)  # 결과: True False

# 조건문

if (2 > 1):
    print('hello')  # 결과 : hello

if not 2 > 1:
    print('hello')  # 결과 : 'null'

if (1 > 0) and (0 > 2):
    print("world")  # 결과: 'null'

if (1 > 0) or (2 > 4):
    print('world')  # 결과: world

if (a > 1):
    print("hello")
else:
    print("hi")  # (a = 1)  결과: hi

if (b > 1):
    print("oh")
elif (b > 3):
    print("yeah")  # (b = 3) 결과: oh

# 함수

print("철수야 안녕 영희야 안녕")
print("모두 안녕")


# ↑ 위 문구들을 반복해야하는 상황 => 함수로 묶음

def chat():
    print("철수야 안녕 영희야 안녕")
    print("모두 안녕")


chat()  # 결과: 철수야 안녕 영희야 안녕 \n 모두 안녕


def chat2(name1, name2):
    print(name1 + ": 철수야 안녕 영희야 안녕")
    print(name2 + ": 모두 안녕")


chat2('김철수철수', '이영희영희')  # 결과: 김철수철수: 철수야 안녕 영희야 안녕\n 이영희영희: 모두 안녕


def chat3(name, name2, age):
    print("%s : %s야 안녕 너는 몇살이니" % (name, name2))
    print("%s : 나는 %d살" % (name2, age))


chat3('김희상', '이순재', 23)  # 김희상 : 이순재야 안녕 너는 몇살이니\n 이순재 : 나는 23살


def dsum(a, b):
    sum = a + b
    return sum


print(dsum(1, 2))  # 반납된 sum을 출력 결과: 3
d = dsum(5, 2)
print(d)  # 결과: 7

# 반복문


for i in range(10):
    print(i)
    print("반복문 예제 출력문입니다")  # 0\n 반복문 예제 출력문입니다\n 1\n 반복문 예제 출력문입니다\n 2\n 반복문 예제 출력문입니다\n •••

i = 0

while i < 3:  # 만약에 i>3이 아닌 True일 경우 무한 루프
    print(str(i) + "반복문 예제 출력문입니다")
    i += 1  # 결과: 0반복문 예제 출력문입니다\n 1반복문 예제 출력문입니다\n 2반복문 예제 출력문입니다

t = 0
while True:
    print(str(t) + "반복문 예제3 출력문입니다")
    t += 1  # 결과: 0반복문 예제3 출력문입니다\n 1반복문 예제3 출력문입니다\n 2반복문3 예제 출력문입니다 \n 3반복문3 예제3 출력문입니다 \n 4반복문3 예제3 출력문입니다
    if (t > 4):
        break

y = 0
while y < 3:  # 만약에 i>3이 아닌 True일 경우 무한 루프
    print(str(y) + "반복문 예제4 출력문입니다")

    y += 1
    if (y < 2):
        continue

    print("continue 실험입니다")  # # #0반복문 예제4 출력문입니다 (y=0) -> (y=1)
    # 1반복문 예제4 출력문입니다 (y=1)-> (y=2)
    # continue 실험입니다 (y<2 false)
    # 2반복문 예제4 출력문입니다 (y=2->y=3)
    # continue 실험입니다 (y=3<2 false)

# 리스트

# 리스트: 요소들을 여러개 그룹으로 묶는것
u = list()
u = ["a", "b", "c"]
o = ["hello", 1, 2, 3]

print(u, o)  # 결과: ['a', 'b', 'c'] ['hello', 1, 2, 3]
print(u + o)  # 결과: ['a', 'b', 'c', 'hello', 1, 2, 3]
print(u[2])  # 결과: c

u[2] = 10  # 요소 바꾸기
print(u[2])  # 결과: 10

p = [8, 6, 4, 26, 9, 5, 1]
print(len(o))  # 결과: 4 (리스트의 길이를 보여주는 함수:len())
print(sorted(p))  # 결과: [1, 4, 5, 6, 8, 9, 26] (리스트 요소를 정렬해주는 함수: sorted())
print(sum(p))  # 결과: 59 (리스트 내부 요소(정수)들을 모두 더하는 함수: sum())

# 리스트 p를 순차적으로 순회하는 n
for n in p:
    print(n)  # 결과:8\n6\n4\n26\n9\n5\n1\n

print(p.index(1))  # 결과: 6(요소 1의 위치 찾기)
print("hello" in o)  # 결과: True ("hello" 라는 요소가 리스트 o 에 있는지 확인)

# 튜플

s = tuple()
d = ("a", 'b', 'c')
f = ('hello', 1, 2)
s = (1, 2, 3)
print(s, d, f)  # 결과: (1, 2, 3) ('a', 'b', 'c') ('hello', 1, 2)

# s[0] = 4 # 결과: TypeError: 'tuple' object does not support item assignment (튜플은 내부 요소를 후천적으로 바꿀 수 없다!)
# 리스트 = 가변(요소 바꾸기 가능) //  튜플 = 불변(요소 바꾸기 불가능)

# 딕셔너리

# 딕셔너리는 key와 value로 이루어져 있다.
h = {
    "name": "조준기",
    "age": 25
}
# key = "name" "age" // value = "조준기" 25
print(h)  # 결과: {'name': '조준기', 'age': 25}
print(h["name"])  # 결과: 조준기
print(h["age"])  # 결과: 25

print("age" in h)  # 결과: True ("age"라는 key가 h 딕셔너리 안에 있나요)

print(h.keys())  # 결과: dict_keys(['name', 'age'])
print(h.values())  # 결과: dict_values(['조준기',25])

for key in h:
    print(key)
    print(h[key])  # 결과: name \n 조준기 \n age \n 25

# 딕셔너리는 value값을 조정 가능하다.

h["name"] = "차태현"

print(h["name"])  # 결과: 차태현

h["school"] = "광운"

print(h)  # 결과: {'name': '차태현', 'age': 25, 'school': '광운'} (딕셔너리는 새로운 key 와 value를 추가할 수 있다.)

## Q. list = ['a','b','c','a','b','a','c','c','b','b','c','b'] 해당 리스트에서 중복된 요소는 각각 몇개인가?
# 1. 변수 및 리스트를 선언한다 2. 반복문으로 각 요소를 순회한다 3. 순회 도중 해당하는 요소들을 카운트한다. (물론 다른 함수가 있을듯하다. nodejs의 filter같은..)

list = ['a', 'b', 'c', 'a', 'b', 'a', 'c', 'c', 'b', 'b', 'c', 'b']

a = 0
b = 0
c = 0
for n in list:
    if (n == 'a'):
        a += 1
    elif (n == 'b'):
        b += 1
    elif (n == 'c'):
        c += 1
    else:
        print("a b c를 제외한 다른 요소도 있습니다.")

print("a 개수 : " + str(a) + "  b 개수: " + str(b) + "  c 개수: " + str(c))  # 결과: a 개수 : 3  b 개수: 5  c 개수: 4

# ↑ 해당 문제는 딕셔너리로 풀었으면 좀 더 깔끔하겠네

dict = {}

for n in list:
    dict[n] = n

print(dict)
