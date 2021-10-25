## 211008(금) 수업내용 오준서
# 파이썬 4장
# 자료구조 - 순서 자료구조 82page
# 1) str 클래스 객체
str_var = str(object='string')
print(str_var)
print(type(str_var))
print(str_var[0])
print(str_var[-1])
# 2) str 클래스 간편 형식
str_var2 = 'string'
print(str_var2)
print(type(str_var2))
print(str_var2[0])
print(str_var[-1])

#단일 리스트 객체 예시 p85
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst :
    print(lst[:i])

#단일 리스트 색인 예시 p86
x = list(range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2])
print(x[1::2])

#중첩 list 객체 예시 p87
# 1)단일 리스트 객체 생성
a = ['a', 'b', 'c']
print(a)
# 2)중첩 리스트 객체 생성
b = [10, 20, a, 5, True, '문자열']
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])

#list 추가, 삭제, 수정, 삽입 예시
# 1)단일 리스트 객체 생성
num = ['one', 'two', 'three', 'four']
print(num)
print(len(num))
# 2)리스트 원소 추가
num.append('five')
print(num)
# 3)리스트 원소 삭제
num.remove('five')
print(num)
# 4)리스트 원소 수정
num[3] = '4'
print(num)
# 5)리스트 원소 삽입
num.insert(0, 'zero')
print(num)
num.insert(4, 'four')
print(num)

#list 연산
# 1)리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x+y
print(z)
# 2)리스트 확장
x.extend(y)
print(x)
# 3)리스트 추가
x.append(y)
print(x)
# 4)리스트 두 배 확장
lst = [1,2,3,4]
result = lst * 2
print(result)

#리스트 정렬과 요소 검사
# 1)리스트 정렬
print(result)
result.sort() #오름차순 정렬
print(result)
result.sort(reverse = True) #내림차순 정렬
print(result)

# 2)리스트 요소 검사
import random
r = []
for i in range(5) :
    r.append(random.randint(1,5))
print(r)

if 4 in r :
    print('있음')
else :
    print('없음')

#리스트 내포 p91
## p91 추가설명
## 변수 = [값1(T) if 조건문 else 값2(F) for 변수 in 열거형객체]

# 1) 변수 = [실행문 for ]
x = [2, 4, 1, 5, 7]
lst = [ i**2 for i in x]
print(lst)

# 2) 변수 = [실행문 for if ]
num = list(range(1,11))
print(num)
lst2 = [i * 2 for i in num if i % 2 == 0]
print(lst2)

#튜플 객체 p93
t = (1,) #튜플에 원소를 한개만 넣을경우 반드시 콤마를 넣어야 튜플로 인식함
print(type(t))

t2 = (1,2,3,4,5,3)
print(t2)
print(type(t2))
#튜플 색인
t3 = 1, 2, 3, 4
print(type(t3))
print(t2[0], t2[1:4], t2[-1])
#튜플 오름차순 만들어보기
t4 = 1, 9, 4, 3
t5 = t4[0],t4[3],t4[2],t4[1]
print(t5)
#튜플 특정숫자 삭제
t6 = t4[1:3]
print(t6)

#튜플 자료형 변환
lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)
print(type(t3))
#튜플 관련 함수
print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))
print(t3)

#Set p96
# 셋은 중복을 허용하지 않기 때문에 색인을 사용할 수 없다.
# 1)중복불가
s = {1,3,5,3,1}
print(len(s))
print(s)
# 2)요소반복
for d in s :
    print(d, end=' ')
# 3)집합관련
s2 = {3, 6}
print(s.union(s2))
print(s.difference(s2))

print(s.intersection(s2))

# 4) 추가 삭제 함수
s3 = {1, 3, 5}
print(s3)

s3.add(7)
print(s3)
# 원소 삭제  > 리무브와 디스카드의 차이점은??
s3.discard(7)
print(s3)

s3.remove(3)
print(s3)

# 중복제거 활용
gender = {'남', '여', '여', '남'}
sgender = set(gender)
lgender = list(sgender)
print(lgender)

print(lgender[1])

#딕트 객체 p99
# 형식) 변수 = {'키' : '값', '키' : '값', ...}
# 키는 중복 허용x / 값은 중복 허용o
# 튜플은 키값으로 활용 가능
# 1)dict 생성 방법1
dic = dict(key1 = 100, key2= 200, key3= 300)
print(dic)

person = {'name': '홍길동', 'age':35, 'address': '서울시', 'name': '이순신', 'name' = '강감찬'}
print(person)

print(person['name'])