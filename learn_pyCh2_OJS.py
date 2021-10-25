## 211006 수업내용
# 파이썬 2장 p35
# 변수와 메모리 주소
var1 = "hello python"
print(var1)
print(id(var1))

var1 = 100
print(var1)
print(id(var1))

var2 = 150.25
print(var2)
print(id(var2))

# 파이썬 예약어 확인
import keyword
python_keyword = keyword.kwlist # keyword모듈에 포함된 kwlist 변수의 값을 가져옴
print(python_keyword)
print(type(python_keyword))
print(len(python_keyword))

# 변수와 자료형
var1 = "Hello python"
print(var1)
print(type(var1))

var1 = 100
print(var1)
print(type(var1))

var2 = 150.25
print(type(var2))

var3 = True
print(type(var3))

# 자료형 변환
# 실수 > 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)
# 정수 > 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)
# 논리형 > 정수
print(int(True))
print(int(False))
# 문자형 > 정수
st = '10'
print(int(st)**2)

# 산술연산자
num1 = 100
num2 = 20

add = num1 + num2
print('add=', add)
sub = num1 - num2
print(sub)
mul = num1 * num2
print(mul)
div = num1 / num2
print(div)
div2 = num1 % num2
print(div2)
square = num1**2
print(square)

# 관계연산자
# 1)동등비교
bool_result = num1 == num2
print(bool_result)
bool_result = num1 != num2
print(bool_result)
# 2)크기비교
bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)

#논리연산자
log_result = num1 >= 50 and num2 <= 10
print(log_result)
log_result = num1 >= 50 or num2 <= 10
print(log_result)
log_result = num1 >= 50
print(log_result)
log_result = not(num1 >= 50)
print(log_result)

# 대입연산자
# 1)변수에 값 할당(=)
i = tot = 10
i += 1
tot += i
print(i, tot)
# 같은 줄에 중복 출력
print('출력1', end=' , ')
print('출력2')

# 2)변수교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)

# 3)패킹 할당
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1, v2)













#211007 수업내용
oneLine = "this is one line string"
print(oneLine)

multiLine = """this is
multi line
string"""
print(multiLine)

multiLine2 ="this is\nmulti line\nstring"
print(multiLine2)

string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

print("python" + " program")
#print("python-" + 3.7 + ".exe") #error
print("python-" + str(3.7) + ".exe")

print("-"*30)

print(oneLine)
print("문자열 길이 : ", len(oneLine))

print(oneLine[0:4])
print(oneLine[0:2])
print(oneLine[0:8])

print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])

print(oneLine[0::2])

print(oneLine[-6::-1])
print(oneLine[-6:])

print(oneLine[5:3])

subString = oneLine[-11:]
print(subString)

oneLine = "this is one line string"
print('t 글자 수 : ', oneLine.count('t'))

print(oneLine.startswith('this'))
print(oneLine.startswith("That"))

print(oneLine.replace('this', 'that'))

multiLine = """ this is
multi line
string"""
sent = multiLine.split('\n')
print('문장 : ', sent)

words = oneLine.split(' ')
print('단어 :', words)

sent2 = ','.join(words)
print(sent2)
print(type(sent2))

oneLine = "this is 'one \"line\" string'"
print(oneLine)

print('escape 문자 차단')
print('\n출력 이스케이프 문자')

print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 문자')

print('path = ', 'C:\Python \test')
print('path = ', 'C:\Python \\test')
print('path = ', r'C:\Python \test')

#단일 조건문 p60
# 1)예시
var = 3
if var >= 5 :
    print('var = ', var)
    print('var는 5보다 크다')
    print('조건이 참인 경우 실행')

print('항상 실행')

# 2)예시
score = int(input('점수 입력 : '))
if score >= 85 and score <=100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

#중첩 조건문 p62
score = int(input('점수 입력 : '))
grade = ''

if score >= 85 and score <=100 :
    grade = '우수'
elif score >= 70 :
    grade = '보통'
else :
    grade = '저조'

print('당신의 점수는 %d이고, 등급은 %s'%(score, grade))

#삼항 조건문 p63
# 1)일반 조건문
num = 9
result = 0

if num >= 5 :
    result = num * 2
else :
    result = num + 2
print('result = ', result)
# 2)3항 연산자
result2 = num * 2 if num >= 5 else num + 2
print('result2 = ', result2)

#반복문 p64
# 1)카운터와 누적변수
cnt = tot = 0
while cnt < 5 :
    cnt += 1 #cnt = cnt + 1
    tot += cnt #tot = tot +cnt
    print(cnt, tot)

# 2)1 ~ 100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = []

while cnt < 100 :
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        dataset.append(cnt)

print('1 ~ 100 사이 3의 배수 합 = %d' % tot)
print('dataset =', dataset)

#무한루프 p66
numData = []

while True :
    num = int(input("숫자 입력 : "))

    if num % 10 == 0 :
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)

print(numData)

#랜덤 관련 함수 p67
# 1)랜덤 도움말
import random
help(random)
# 2)랜덤 모듈의 함수 도움말
help(random.random)
# 3)0~1 사이 난수 실수
r = random.random()
print('r=', r)
# 4)난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0
while True :
    r = random.random()
    print(r)

    if r < 0.01 :
        break
    else:
        cnt += 1
print('난수 개수 = ', cnt)

#랜덤 관련 함수 p68
# 1)모듈 관련 함수 도움말
help(random.randint)
# [1, 5] -> 1 <= x <= 5
# [1, 5) -> 1 <= x < 5 ???
# (1, 5) ->  1 < x < 5 ???

# 2)이름 list에 전체 이름, 특정 이름 출력
names = ["홍길동", "이순신", "유관순"]
print(names)
print(names[2])

# 3)list에서 자료 유무 확인하기
if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

# 4)난수 정수로 이름 선택하기
idx = random.randint(0,2)
print(names[idx])

#break, continue 사용예 p69
i = 0
while i < 10:
    i += 1
    if i == 3 :
        continue
    if i == 6:
        break
    print(i, end= '')

#for 반복문 p70
string = "홍길동"
print(len(string))

for s in string :
    print(s)

lstset = [1,2,3,4,5]

for e in lstset :
    print('원소 : ' , e)

num1 = range(10)
print('num1 : ', num1)

list(range(10))

num2 = range(1,10)
print('num2: ', num2)

list(range(1,10))

list(range(1,10,3))

for n in num1 :
    print(n, end=' ')
#print()
for n in num2 :
    print(n, end=' ')
# print()
for n in num3 :
    print(n, end=' ')

#list 자료구조 예 p73
lst = []
for i in range(10) :
    r = random.randint(1,10)
    lst.append(r)

print('lst = ', lst)

for i in range(10) :
    print(lst[i]*0.25, end =' ')
    print()