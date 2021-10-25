## 211012 오준서
# 파이썬 4장 연습문제

#문제1
# 다음lst 변수를 대상으로 각 단계별로 list를 연산하시오
lst = [10, 1, 5, 2]

# 단계1) lst 원소를 2배 생성하여 result 변수에 저장 및 출력하기
result = lst * 2
result

# 단계2) lst의 첫 번째 원소에 2를 곱하여 result 변수에 추가 및 출력하기
result.append(20)
result

# 단계3) result의 홀수 번째 원소만 result2 변수에 추가 및 출력하기
result2 = result[::2] # [10, 5, 10, 5, 20]
# 출력 결과 예시는 짝수 번째 원소로 보임
result3 = result[1::2] #[1, 2, 1, 2]


#문제2
# list 원소 추가 및 요소 검사하기
# A형) list 크기를 키보드로 입력 받은 후, 입력 받은 크기만큼 임의 숫자를 list에 추가하고, list의 크기를 출력하시오.
A = int(input('vector 수: '))
lst = []
for i in range(A) :
    x = int(input(' '))
    lst.append(x)

print('vector 크기: ', A)

# B형) list 크기를 키보드로 입력 받은 후, 입력 받은 크기만큼 임의 숫자를 list에 추가한다.
# 이후 list에서 찾을 값을 키보드로 입력한 후 해당 값이 list에 있으면 "YES", 없으면 NO"를 출력하시오.
B = int(input('vector 수: '))
lst = []
for i in range(B) :
    x = int(input(' '))
    lst.append(int(x))

if int(input()) in lst :
    print("YES")
else :
    print("NO")


#문제3
# A형) message 변수를 대상으로 'spam'원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
# <조건> list + for 형식 적용
message = ['spam', 'ham', 'spam', 'ham', 'spam']
dummy = [1 if msg == 'spam' else 0 for msg in message]
dummy

# B형) message 변수를 대상으로 'spam'원소만 추출하여 spam_list에 추가하시오
# <조건> list + for + if 형식 적용
spams = [msg for msg in message if msg == 'spam']
print(spams)

#문제4
# position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수를 출력하시오.
position = ['과장', '부장', '대리', '사장', '대리', '과장']
cnt = {}
for key in position :
    cnt[key] = cnt.get(key, 0) +1
print('중복되지 않은 직위 : ', list(set(position)))
print('각 직위별 빈도수 : ', cnt)

#풀이
import random
size = int(input('vector 수 :'))
lst = []
for i in range(size):
    lst.append(random.randint(1,10))

print(lst)
print('vector 크기: ', len(lst))
#B형
if int(input('무슨 숫자가 있을까? ')) in lst:
    print('yes')
else:
    print('no')
