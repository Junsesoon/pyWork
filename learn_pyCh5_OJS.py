## 211013 수업내용
# 파이썬 5장 프로그램 블록 만들기
# builtins 함수
help(len)
dataset = list(range(1,6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

#import 함수
import statistics
from statistics import variance, stdev

print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))
print('표본 분산=', variance(dataset))
print('표본 표준편차=', stdev(dataset))

import builtins
dir(builtins)

#builtins 내장함수
# abs(x)
abs(10)
abs(-10)
abs(-123.45)
# all(iterable): 모든 요소가 True 일 때 True를 반환(0이 아닌 숫자는 True로 해석)
all([1, True, 10, -15.2])
all([1, True, 0, -15.2])
all([1, False, 0, -15.2])
# anyl(iterable): 하나 이상의 요소가 True일 때 True를 반환한다.(0은 False로 해석)
any([1, False, 0, -15.2])
any([False, 0, 0])
# bin(number): 10진수 정수를 2진수로 반환한다. 2진수는 '0b' 문자열로 시작한다.
bin(10)
bin(15)
# dir(x): 객체 x에서 제공하는 변수, 내장함수, 내장클래스의 목록 반환
# x의 멤버들은 'x.멤버' 형식으로 호출한다.
x = [1,2,3,4,5]
dir(x)
x.append(6)
y = {1,2,3,4,5}
dir(y)
# eval(expr): 문자열 수식을 인수로 받아서 계산 가능한 파이썬 수식으로 변환
eval("10 + 20")
eval(10 + "20 * 30") # ERROR
eval("10 + 20 * 30")
eval("20 * 30") + 10
# hex(number): 10진수 정수를 16진수로 반환.(16진수는 '0x'문자열로 시작)
hex(10)
hex(15)
hex(64)
# oct(number): 10진수 정수를 8진수로 반환.(8진수는 '0o'문자열로 시작한다.
oct(10)
oct(7)
oct(8)
# ord(character): character를 아스키 값으로 반환한다.(숫자 0은 48, A는 65, a는 97이다)
ord('0')
ord('9')
ord('A')
ord('Z')
ord('a')
ord('z')
# pow(x,y): x에 대한 y의 제곱을 계산하여 반환한다.
pow(10, 2)
pow(10, 3)
pow(10, -1)
pow(10, -2)
# round(number): 실수를 인수로 하여 반올림을 수행하는 결과를 반환한다.
round(3.14159)
round(3.14159, 3) #소수점 3자리
# sorted(iterable): 반복 가능한 원소들을 대상으로 오름차순 또는 내림차순 정렬한 결과를 반환한다.
sorted([3,2,1,5])
sorted([3,2,1,5], reverse=True)
# zip(iterable*): 반복가능한 객체와 객체 간의 원소들을 묶어서 튜플로 반환
# zip() 함수에서 반환된 결과를 확인하기 위해서 list 클래스를 이용하여 리스트 자료구조로 변환해야 한다.
zip([1,3,5], [2,4,6])
list(zip([1,3,5], [2,4,6]))

############################
# 사용자정의함수 123page
# 1) 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')
userFunc1()
# 2) 인수가 있는 함수
def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z=', z)
userFunc2(10, 20)
# 3) return 있는 함수
def userFunc3(x, y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return tot, sub, mul, div
# 실인수: 키보드 입력
x = int(input('x 입력: '))
y = int(input('y 입력: '))

t, s, m, d = userFunc3(x, y)
print('tot =', t)
print('sub =', s)
print('mul =', m)
print('div =', d)

# 산포도 구하기 125page
# 분산과 표준편차 함수
from statistics import mean, variance
from math import sqrt
dataset = [2, 4, 5, 6, 1, 8]
# 1) 산술평균
def Avg(data):
    avg = mean(data)
    return avg
print('산술평균=', Avg(dataset))
# 2) 분산/표준편차
def var_sd(data) :
    avg = Avg(data) # 함수 호출
    # list 내포
    diff = [(d - avg)**2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)
    return var, sd
# 3) 함수 호출
v, s = var_sd(dataset)
print('분산 =', v)
print('표준편차=', s)

# 피타고라스 정의 함수
def pytha(s, t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print('3변의 길이 : ', a,b,c)

pytha(2, 1)

# 몬테카를로 시뮬레이션
import random
# 단계 1: 동전 앞면과 뒷면의 난수 확률분포 함수 정의
def coin(n):
    result = []
    for i in range(n) :
        r = random.randint(0,1)
        if (r == 1) :
            result.append(1)
        else:
            result.append(0)
    return result
print(coin(10))

# 단계 2: 몬테카를로 시뮬레이션 함수 정의
def montaCoin(n) :
    cnt = 0
    for i in range(n) :
        cnt += coin(1)[0]
    result = cnt / n
    return result

# 단계 3: 몬테카를로 시뮬레이션 함수 호출
print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))

# 특수함수 129page
# 가변인수 함수
# 형식: def 함수명(매개변수, *매개변수, **매개변수):
# 1) 튜플형 가변인수
def Func1(name, *names):
    print(name)
    print(names)

Func1("홍길동", "이순신", "유관순")

from statistics import mean, variance, stdev
# 2) 통계량 구하는 함수
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'

# statis 함수 호출
print('avg=', statis('avg', 1,2,3,4,5))
print('var=', statis('var', 1,2,3,4,5))
print('std=', statis('std', 1,2,3,4,5))

# 3) 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

emp_func('홍길동', 35, addr='서울시', height=175, weight=65)

# 람다 함수 131page
# 형식: lambda 매개변수: 실행문(반환값)
# 1) 일반 함수
def Adder(x, y):
    add = x + y
    return add
print('add=', Adder(10, 20))

# 2) 람다 함수
print('add=', (lambda x, y: x + y)(10, 20))

# 스코프
# 1) 지역변수
x = 50
def local_func(x):
    x += 50
local_func(x)
print('x=', x)

# 2) 전역변수
def global_func():
    global x
    x += 50

global_func()
print('x=', x)

# 중첩함수 133page
# 일급함수와 함수 클로저
# 1) 일급 함수
def a(): # outer
    print('a 함수')
    def b(): # inner
        print('b 함수')
    return b
b = a() # 외부 함수 호출: a 함수
b() # 내부 함수 호출 : b 함수

# 2) 함수 클로저
data = list(range(1, 101))
def outer_func(data):
    dataSet = data
    # inner
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg # inner 반환
# 외부 함수 호출: data 생성
tot, avg = outer_func(data)
# 내부 함수 호출
tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)

# 산포도를 구하는 중첩함수
from statistics import mean
from math import sqrt
data = [4, 5, 3.5, 2.5, 6.3, 5.5]
# 1) 외부 함수: 산포도 함수
def scattering_func(data): # outer
    dataSet = data
    # 2) 내부 함수: 산술평균 반환
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    # 3) 내부 함수: 분산 반환
    def var_func(avg):
        diff = [(data - avg)**2 for data in dataSet]
        print(sum(diff)) # 차의 합
        var_val = sum(diff) / (len(dataSet) -1 )
        return var_val
    # 4) 내부 함수: 표준편차 반환
    def std_func(var):
        std_val = sqrt(var)
        return std_val
    # 함수 클로저 반환
    return avg_func, var_func, std_func
#! 5) 외부 함수 호출
avg, var, std = scattering_func(data)
# 6) 내부 함수 호출
print('평균: ', avg())
print('분산: ', var(avg()))
print('표준편차: ', std(var(avg())))

## 획득자와 지정자~