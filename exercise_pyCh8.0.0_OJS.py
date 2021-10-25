## 211022 오준서
# 파이썬 8장 연습문제

# 문제1
# ftest.txt파일을 읽어서 다음과 같이 줄 수와 단어 수를 카운트 하시오.
# 조건1) 문장은 '\n'을 구분자로 한다.
# 조건2) 단어는 공백을 구분자로 한다.
file = open('c:/james/pyEducation/ch8_meterial/data/ftest.txt', mode = 'r')
lines = file.readlines()
docs = []
words = []

for line in lines:
    docs.append(line.strip())
for word in docs:
    words.extend(word.split(sep=' '))

print('문장 내용\n',docs,'\n문장 수: %d'%(len(docs)))
print('단어 내용\n',words,'\n단어 수: %d'%(len(words)))

# 문제2
# emp.csv 파일을 읽어서 다음 출력 예시와 같이 출력하시오.
# 예시)
# 관측치 길이: 5
# 전체 평균 급여: 370.0
# 최저 급여: 150, 이름: 홍길동
# 최고 급여: 500, 이름: 강감찬
import pandas as pd
emp = pd.read_csv('c:/james/pyEducation/ch8_meterial/data/emp.csv', encoding='utf-8')
print(emp.info())

name = emp.Name
pay = emp['Pay']

for i in range(len(pay)):
    if min(pay) == pay[i]:
        mini = name[i]
    elif max(pay) == pay[i]:
        maxi = name[i]

# 결과값 출력
print('관측치 길이: ',len(emp))
print('전체 평균 급여: ',format(mean(pay),'.1f'))
print('최저 급여: %d, 이름: %s'%(min(pay),mini))
print('최고 급여: %d, 이름: %s'%(max(pay),maxi))