## 211014 오준서
# 파이썬 5장 연습문제

##문제1
# 다음 height 변수에 별(star)의 층수를 입력하면 각 층 마다 별의 개수가 한 개씩
# 증가하여 출력되고, 마지막 줄에 별의 개수가 출력되도록 함수의 빈 칸을 채우시오.
def StarCount(height):
    if height == 1 :
        print('*')
        return 1
    else:
        st = StarCount(height-1) + height
        print('*'*height)
        return st

# 키보드 입력
height = int(input('height: '))
# start 개수 출력
print('start 개수 : %d'%StarCount(height))



##문제2
# 중첩함수를 적용하여 다음<조건>에 맞게 은행계좌 함수의 빈 칸을 채우시오.
# <조건1> 외부함수: bank_account(): 잔액(balance) outer변수
# <조건2> 내부함수: getBalance(): 잔액확인
#                 deposit(money): 입금하기
#                 withdraw(money): 출금하기
# <조건3> 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력
# <조건4> 기타 나머지는 출력 예시 참조`
def bank_account(bal) :
    balance = bal # 잔액 초기화
    def getBalance(): # 잔액확인(getter)
        return balance
    def deposit(money) : # 입금하기(setter)
        nonlocal balance
        balance += money
        return balance
    def withdraw(money) : # 출금하기
        nonlocal balance
        if balance >= money:
            balance -= money
            return balance
        else:
            return print("잔액이 부족합니다.")
    return getBalance, deposit, withdraw

bal = int(input("최초 계좌의 잔액을 입력하세요: "))
get, dep, wit = bank_account(bal)
print('현재 계좌 잔액은: %d원 입니다.' %get())
depm = int(input("입금액을 입력하세요: "))
print('%d원 입금후 잔액은 %d원 입니다.'%(depm, dep(depm)))
witm = int(input("출금액을 입력하세요: "))
print('%d원 출금후 잔액은 %d원 입니다.'%(witm, wit(witm)))



##문제3
# 패토리얼(Factorial)을 계산하는 재귀함수의 빈 칸을 채우시오.
# 재귀 함수 정의
def Factorial(n) :
    if n == 1 :
        return 1
    else :
        Factorial(n-1)
        result_fact = n * Factorial(n-1)
        return result_fact

# 함수 호출
result_fact = Factorial(5)
# result_fact = Factorial(int(input('숫자를 입력하세요'))) # 입력받아서 처리하기
print('패토리얼 결과: ', result_fact)
