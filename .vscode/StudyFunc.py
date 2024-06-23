# 함수 Func, parameter value
def open_account():
    print("계좌 신설")

def deposit(balance,  money):
    print("입금이 완료 되었습니다")
    print("잔액은 {0} 입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance > money:
        print("출금이 완료 되었습니다. {0} 원입니다.".format(balance-money))
        return balance-money
    else:
        print("잔액이 부족합니다. 잔액은 {0} 입니다.".format(balance))

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000) # 입금
# balance = withdraw(balance, 500) # 출금
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원 입니다. 잔액은 {1} 입니다".format(commission, balance))
