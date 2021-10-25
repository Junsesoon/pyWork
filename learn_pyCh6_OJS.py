## 211015(금) 수업내용 오준서
# 파이썬 6장
# 함수와 클래스 150page
# 1) 함수정의
def calc_func(a,b) :
    x=a
    y=b
    def plus():
        p=x+y
        return p
    def minus():
        m=x-y
        return m
    return plus, minus
# 2) 함수호출
p, m = calc_func(10, 20)
print('plus =', p())
print('minus=', m())
# 3) 클래스 정의
class calc_class :
    x = y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m
# 4) 객체 생성
obj = calc_class(10, 20)
# 5) 멤버 호출
print('plus= ', obj.plus())
print('minus= ', obj.minus())


# 클래스 구성요소
# 1) 멤버 변수
class Car:
    cc = 0
    door = 0
    carType = None
    # 2) 생성자
    def __init__(self, cc, door, carType):
        self.cc = cc
        self.door = door
        self.carType = carType
    # 3) 메서드
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s"%(self.cc, self.door, self.carType))
# 4) 객체 생성
car1 = Car(2000, 4, "승용차")
car2 = Car(3000, 5, "SUV")
# 5) 멤버 호출
car1.display()
car2.display()


# 생성자 155page
# 1) 생성자 이용 멤버변수 초기화
class multiply :
    x = y = 0
    # 생성자: 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 메서드
    def mul(self):
        return self.x * self.y
obj = multiply(10, 20)
print('곱셈 =', obj.mul())
# 2) 메서드 이용 멤버변수 초기화
class multiply2 :
    x = y = 0
    # 생성자 없음: 기본 생성자 제공
    def __init__(self):
        pass
    # 메서드: 멤버변수 초기화
    def data(self, x, y):
        self.x = x
        self.y = y

    # 메서드: 곱셈
    def mul(self):
        return self.x * self.y

obj = multiply2() # 기본 생성자
obj.data(10,20) # 동적 멤버변수 생성
print('곱셈= ', obj.mul())


#############################################
#cf) 소멸자 157page
class multiply :
    # 생성자: 객체 생성 + 멤버변수 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 소멸자: 객체 소멸
    def __del__(self):
        del self.x
        del self.y

#############################################


# self 명령어
class multiply3 :
    # 멤버변수, 생성자 없음
    # 동적 멤버변수 생성/초기화
    def data(self, x, y):
        self.x = x
        self.y = y
    # 곱셈 연산
    def mul(self):
        result = self.x * self.y
        self.display(result) # 메서드 호출

    # 결과 출력
    def display(selfself, result):
        print("곱셈 = %d" %(result))

obj = multiply3()
obj.data(10, 20)
obj.mul()


# 클래스 멤버
class DatePro:
    # 1) 멤버 변수
    content = "날짜 처리 클래스"
    # 2) 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    # 3) 객체 메서드
    def display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))
    # 4) 클래스 메서드
    @classmethod #함수 장식자
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

    # 5) 객체 멤버
date = DatePro(1995, 10, 25)
print(date.content)
print(date.year)
date.display()

# 6) 클래스 멤버
print(DatePro.content)
DatePro.date_string('19951025')

# 캡슐화 161page
class Account:
    # 1) 은닉 멤버변수
    __balance = 0
    __accName = None
    __accNo = None
    # 2) 생성자: 멤버변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no
    # 3) 계좌정보 확인: Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo
    # 4) 입금하기: Setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return
        self.__balance += money
        # 5) 출금하기: Setter
    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return
        self.__balance -= money
# 6) object 생성
acc = Account(1000, '홍길동', '125-152-4125-41')
# 7) Getter 호출
#acc.__balance
bal = acc.getBalance()
print('계좌정보: ', bal)
# 8) Seteer 호출
acc.deposit(10000)
bal = acc.getBalance()
print('계좌정보: ', bal)


# 클래스 상속 p164
# 1) 부모 클래스
class Super :
    # 생성자: 동적멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 메서드
    def display(self):
        print('name : %s, age: %d'%(self.name, self.age))
        sup = Super('부모', 55)
        sup.display() # 부모 멤버 호출
# 2) 자식 클래스
class Sub(super) : # 클래스 상속
    gender = None # 자식 멤버
    # 3) 생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # 4) 메서드 확장
    def display(self):
        print('name: %s, age : %d, gender : %s'%(self.name, self.age, self.gender))
sub = Sub('자식', 25, '여자')
sub.display(parents.__init__)

# super 클래스 166page
class Parent:
    # 생성자: 객체 + 초기화
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # 멤버 함수(method)
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))

# 부모 클래스 객체 생성
p = Parent('홍길동', '회사원')
p.display()

# 2) 자식 클래스
class Children(Parent): # Parent 클래스 상속
    gender = None # 자식 클래스 멤버변수 추가
    # 3) 자식 클래스 멤버변수 추가
    def __init__(self, name, job, gender):
        # 부모 클래스 생성자 호출
        super().__init__(name, job) # name, job 초기화
        self.gender = gender
    # 멤버 함수(method)
    def display(self):
        print('name : {}, job : {}, gender : {}'.format(self.name, self.job, self.gender))

# 자식 클래스 객체 생성
chil = Children("이순신", "해군 장군", "남자")
chil.display()

# 메서드 재정의 168page
# 1) 부모클래스
class Employee:
    name = None
    pay = 0
    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass

# 2) 자식클래스: 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name) # 부모 생성자 호출
    def pay_calc(self, base, bonus):
        self.pay = base + bonus # 급여 = 기본급 + 상여금
        print('총 수령액 : ', format(self.pay, '3,d'), '원')

# 3) 자식클래스: 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name) # 부모 생성자 호출
    def pay_calc(self, tpay, time):
        self.pay = tpay * time # 급여 = 작업시간 * 시급
        print('총 수령액 : ', format(self.pay, '3,d'), '원')

# 4) 객체 생성
p = Permanent("이순신")
p.pay_calc(3000000, 200000)

t = Temporary("홍길동")
t.pay_calc(15000, 80)

# 다형성
# 1) 부모 클래스
class Flight:
    # 부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')
# 2) 자식 클래스: 비행기
class Airplane(Flight):
    # 함수 재정의
    def fly(self):
        print('비행기가 날다.')
# 2) 자식 클래스: 새
class Bird(Flight):
    # 함수 재정의
    def fly(self):
        print('새가 날다')

# 2) 자식 클래스: 종이비행기
class PaperAirplane(Flight):
    # 함수 재정의
    def fly(self):
        print('종이 비행기가 날다.')

# 3) 객체 생성
# 부모 객체 = 자식 객체(자식1, 자식2)
flight = Flight() # 부모 클래스 객체
air = Airplane() # 자식1 클래스 객체
bird = Bird() # 자식2 클래스 객체
paper = PaperAirplane() # 자식3 클래스 객체

# 4) 다형성
flight.fly()

flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()

# 내장클래스 173page
# builtins 모듈 내장클래스
# 1) 리스트 열거형 객체 이용
lst = [1,3,5]
for i, c in enumerate(lst):
    print('색인 : ', i, end=' ')
    print('내용 : ', c)

# 2) 딕트 이용
dit = {'name':'홍길동', 'job':'회사원', 'addr':'서울시'}
for i, k in enumerate(dit):
    print('순서 :', i, end=', ')
    print('키 :', k, end=', ')
    print('값 :', dit[k])

# import 모듈 내장클래스
# 1) 모듈 내장클래스 import
import datetime
from datetime import date, time
# 2) date 클래스
help(date)
today = date(2021, 10, 18)
print(today) # date 객체 정보
# date 객체 멤버변수 호출
print(today.year)
print(today.month)
print(today.day)
#date 객체 메서드 호출
w = today.weekday()
print('요일 정보 : ', w)
# 3) time 클래스
help(time)

currTime = time(11, 9, 30)
print(currTime)
# time 객체 멤버변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)
# time 객체 메서드 호출
isoTime = currTime.isoformat()
print(isoTime)

#라이브러리 import 176page
# scattering 모듈 내용
# 1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt
# 2) 산술평균 함수
def Avg(data) :
    avg = mean(data)
    return avg
# 3) 분산/표준편차 함수
def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]
    var = sum(diff) / (len(data) -1)
    sd = sqrt(var)

    return var, sd

# module 모듈 내용
# 1) 모듈 추가(방법1)
# 형식) import 패키지명.모듈명
import chapter06.myPackage.scattering

# 데이터 셋
data = [1, 3, 1.5, 2, 1, 3.2]
# 산술평균 함수 호출
print('평균 : ', chapter06.myPackage.scattering.Avg(data)) #? 앞에 'chapter06'을 붙이면 작동 안함
# 분산과 표준편차 함수 호출
var, sd = myPackage.scattering.var_sd(data)
print('분산 :', var)
print('표준편차 : ', sd)

# 2) 모듈 추가(방법2)
# 형식) from 패키지명.모듈명 import 함수명
from myPackgae.scattering import Avg, var_sd

print('평균 : ', Avg(data))

var, sd = var_sd(data)
print('분산 :', var)
print('표준편차 :', sd)

# 시작점(main) 만들기
# 형식: if __name__ == "__main__" : # 프로그램 시작점
#            명령문
# 1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt
# 2) 산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg
# 3) 분산/표준편차 함수
def var_sd(data):
    avg = Avg(data)
    diff = [(d-avg) ** 2 for d in data]
    var = sum(diff) / (len(data) -1)
    sd = sqrt(var)
    return var, sd
# 프로그램 시작점
if __name__ == "__main__" :
    data = [1, 3, 5, 7]
    print('평균=', Avg(data))
    var, sd = var_sd(data)
    print('분산=', var)
    print('표준편차=', sd)

# 프로그램 시작점이 없는 경우
# 1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

# 2) 산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg

# 3) 분산/표준편차 함수
def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg) ** 2 for d in data]
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd

# 프로그램 시작점 없음
data = [1, 3, 5, 7]
print('평균=', Avg(data))
var, sd = var_sd(data)
print('분산=', var)
print('표준편차=', sd)