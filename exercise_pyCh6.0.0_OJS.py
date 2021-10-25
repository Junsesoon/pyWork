## 211019 오준서
# 파이썬 6장 연습문제

# 문제1
# 다음과 같은 <처리조건>에 맞게 Rectangle 클래스를 작성하시오.
# 조건1) 멤버변수: 가로(width), 세로(height)
# 조건2) 생성자: 가로(width), 세로(height) 멤버 변수 초기화
# 조건3) 메서드(area_calc): 사각형의 넓이를 구하는 함수
# 조건4) 메서드(circum_calc): 사각형의 둘레를 구하는 함수
print('사각형의 넓이와 둘레를 계산합니다')
w = int(input('사각형의 가로 입력: '))
h = int(input('사각형의 높이 입력: '))

class rectangle:
    width = height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        return area

    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum

rec = rectangle(w, h)
area = rec.area_calc()
print('사각형의 넓이 : ', area)
circum = rec.circum_calc()
print('사각형의 둘레 : ', circum)



# 문제2
# 동적 멤버 변수를 생성하여 다음과 같은 산포도를 구하는 클래스를 정의하시오.
from statistics import mean
from math import sqrt
x = [5, 9, 1, 7, 4, 6]

# 산포도 클래스
class Scattering:
    # 생성자
    def __init__(self,x):
        self.x = x
    # 메서드: 분산(var_func) 125page 참조: 분산, 표준편차 공식
    def var_func(self):
        avg = mean(x)
        diff = [(i - avg)**2 for i in x]
        var = sum(diff) / (len(x)-1)
        return var
    # 메서드: 표준편차(std_func)
    def std_func(self):
        sd = sqrt(var) #? 전역변수 설정법 확인필요
        return sd

scat = Scattering(x)
var = scat.var_func() #! 위아래 순서 못바꿈
sd = scat.std_func()
print('x의 분산', var,'\n표준편차', sd)



# 문제3
# 다음과 같은 <처리조건>에 맞게 Person 클래스를 작성하시오.
# 조건1) 멤버 변수: 이름(name), 성별(gender), 나이(age)
# 조건2) 생성자: 이름, 성별, 나이 초기화
# 조건3) 메서드: display(이름, 성별, 나이 출력 기능)
# 조건4) 기타 세부내용은 <출력 결과 예시> 참조

class Person:
    #생성자
    def __init__(self,name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    # 메서드
    def display(self):
        if self.gender == 'male' :
            print("이름: {}, 성별: {}\n나이: {}".format(self.name, "남자", self.age))
        else :
            print("이름: {}, 성별: {}\n나이: {}".format(self.name, "여자", self.age))

# 입력
name = input('이름: ')
age = int(input('나이: '))
gender = input('성별(male/female) : ')
# 객체 생성
p = Person(age, name, gender) # 생성자 이용 전역변수 초기화
p.display()



# 문제4
# 다음과 같은 <처리조건>에 맞게 Employee 클래스를 상속받아서 Permanent와 Temporary 클래스를 구현하시오.
# 조건1) 키보드로 정규직과 임시직을 구분한다.
# 조건2) 정규직인 경우에는 기본급과 상여금을 입력 받아서 급여를 계산한다.
# 조건3) 임시직인 경우에는 작업시간과 시급을 입력 받아서 급여를 계산한다.

# 부모 클래스
class Employee :
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
# 자식 클래스 - 정규직
class Permanent(Employee):
    def __init__(self, name, gold, bon):
        super().__init__(name)
        self.sal = gold + bon

# 자식 클래스 - 임시직
class Temporary(Employee):
    def __init__(self, name, time, timepay):
        super().__init__(name)
        self.pay = time * timepay

emp = input('고용형태 선택(정규직<P>, 임시적<T>) : ')
if emp == 'P' or emp == 'p' :
    name = input('이름: ')
    sal = int(input('기본급: '))
    bon = int(input('상여금: '))
    p = Permanent(name, sal, bon)
    print('고용형태 : 정규직')
    print('이름: ', p.name)
    print('급여: ', format(p.sal, '3,d'))
elif emp == 'T' or emp == 't' :
    name = input('이름: ')
    time = int(input('작업시간: '))
    timepay = int(input('시급: '))
    t = Temporary(name, time, timepay)
    print('고용형태: 임시직')
    print('이름: ', t.name)
    print('급여: ', format(t.pay, '3,d'))
else :
    print('='*30, '\n입력 오류')


# 문제5
# 조건1) 패키지명: myCalcPackage
# 조건2) 모듈명: calcModule.py
# 조건3) 함수명: Add(), Sub(), Mul(), Div()
# 조건4) 호출 모듈명: example.py
from myCalcPackage_OJS.calcModule_OJS import Add, Sub, Mul, Div

x = 10; y = 5
print("x = %d; y= %d 일때" %(x, y))
print("Add = %d" %Add(x, y))
print("Sub = %d" %Sub(x, y))
print("Mul = %d" %Mul(x, y))
print("Div = %.1f" %Div(x, y))