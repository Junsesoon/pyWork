## 211008 오준서
# 파이썬 3장 연습문제

#문제1
# A형) 항공사에서는 짐을 부칠 떄, 10kg 이상이면 수수료 10,000원을 내야한다.
# 만약 10kg 미만이면 수수료는 없다. 사용자의 짐의 무게를 키보드로 입력 받아서
# 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오.
caseA = int(input('짐의 무게는 얼마입니까? '))
if caseA >= 10 :
    print('수수료는 10,000원 입니다')
else :
    print('수수료는 없습니다.')

# B형) 항공사에서는 짐을 부칠 떄, 10kg이상 부터 수수료를 내야한다.
# 수수료는 10의 배수 단위로 10,000원씩 증가한다. 만약 10kg 미만이면 수수료는 없다.
# 사용자의 짐의 무게를 키보드로 입력 받고, 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오.
caseB = int(input('짐의 무게는 얼마입니까?'))
price = (caseB//10) * 10000
if caseB >= 10 :
    print('수수료는 ', format(price, "3,d"), '원 입니다.')
else :
    print("수수료는 없습니다.")

#문제2
# 컴퓨터에 의해서 1~10 사이의 난수가 발생될 때 사용자가 예상되는 숫자를 키보드를 입력한 경우 일치하면
# '~~성공~~' 메시지를 출력하고, 반복을 탈출한다. 만약 사용자가 입력한 수가 난수 보다 더 크면 '더 작은 수 입력'
# 메시지를 출력하고 , 반복을 꼐속한다. 또한 사용자가 입력한 수가 난수 보다 작으면 '더 큰 수 입력' 메시지를
# 출력하고, 반복을 계속한다. 위 내용이 실행될 수 있도록 프로그램의 빈 칸을 채우시오.
import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10)

while True :
    my = int(input('예상 숫자를 입력하시오 : '))
    if my == com :
        break
    elif my > com :
        print("더 작은 수 입력")
    else :
        print("더 큰 수 입력")
print('~~성공~~')

#문제3
# 1~100 사이에서 3의 배수이면서 2의 배수가 아닌 수를 한 줄에 출력하고, 누적합을 출력 하시오.
num1 = 0
print('수열 = ', end='')
for n in range(1, 101) :
    if n % 3 == 0 and n % 2 != 0 :
        print(n, end=' ')
        num1 += n
print('\n누적합 = %d'%num1)




#문제4
# 중첩 반복문을 이용한 '단어 카운트하기(word count)'
# 다음과 같은 multiline의 문자열 객체를 이용하여 단어를 추출하고 단어의 개수를 출력하시오.
multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

cnt = 0
sents = []
words = []
for sen in multiline.split(sep = "\n") :
    sents.append(sen)
#!    print(sen) #for문 작동원리 파악
    for word in sen.split() :
        words.append(word)
        print(word)
        cnt += 1

print('단어 개수 :', cnt)
