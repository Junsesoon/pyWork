## 211025(월) 오준서
# 문제11
# 파일을 쓰기모드로 열어 글을 입력해 저장하고, 다시 파일을 읽기 모드로 열어 화면에 출력하려고 한다.
# 다음 코드가 적절히 구현되도록 빈칸을 채우고 coding하시오.
import os
print(os.getcwd())
f = open("foo.txt", mode='a', encoding='utf8')
f.write('Life is too short, you need python')
f.close()
# f.close() 할 필요 없도록 파일을 열려고 함.
with open("foo.txt",mode='r')as f:
line=f.readline()
print(line)


# 문제12
# 아래 처리조건에 맞게 coding 하여 은행 계좌의 기존잔액, 입금액, 출금액 정보를 가지고
# 현재의 잔액을 구하고 현 잔액에 한달동안의 이자액을 계산하시오.
# 기존잔액: 10000원
# 입금액: 5000원
# 출금액: 3,000원
# 한달동안의 이자율: 2%
# 조건1) 클래스 객체로 작성합니다.
# 조건2) 클래스 내 멤버 변수를 설정합니다.
# 조건3) 클래스 내 생성자를 작성합니다.
# 조건4) 클래스 내 기존잔액, 입금액, 출금액을 이용하여 신규잔액을 계산하는 개체 메서드 작성
# 조건5) 객체 메서드 내에서 실행된 결과 변수가 다른 객체 메서드에서 사용될 수 있도록 설정
# 조건6) 클래스 내 신규잔액을 이용하여 한달동안의 이자액을 계산하는 개체 메서드를 작성
    # 이자= 잔액*이자율
# 조건7) 클래스에 기존잔액, 입금액, 출금액, 이자율을 입력하여 객체를 생성
# 조건8) 생성된 객체에 객체메서드를 사용하여 현재 잔액을 보여줍니다.
# 조건9) 생성된 객체에 객체메서드를 사용하여 한달의 이자액을 보여줍니다.
class account:
    # 멤버변수
    balance = 0 # 잔액
    deposit = 0 # 입금액
    withdraw = 0 # 출금액
    rate = 0 # 한달동안의 이자율
    # 생성자
    def __init__(self, balance, deposit, withdraw, rate):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.rate = rate
    # 메서드 생성: 신규잔액
    def newBal(self):
        return self.balance+self.deposit-self.withdraw
    # 메서드 생성: 이자율
    def interest(self):
        return self.newBal()*self.rate

# 객체 생성: 고객1, 고객2
customer1 = account(10000, 5000, 3000, 0.02) # 기존잔액, 입금액, 출금액, 이자율
customer2 = account(20000, 5000, 3000, 0.02)

# 고객1 멤버 호출
print('현재 잔액은: ',customer1.newBal(),'원 입니다.')
print('예상되는 한달 이자액은 ',customer1.interest(), '원 입니다.')
# 고객2 멤버 호출
print('현재 잔액은: ',customer2.newBal(),'원 입니다.')
print('예상되는 한달 이자액은 ',customer2.interest(), '원 입니다.')