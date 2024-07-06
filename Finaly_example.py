# # 사용자 정의 Error 처리
# class BigNumError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기")
#     num1 = int(input("1 입력 : "))
#     num2 = int(input("2 입력 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumError("입력 값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(int(num1), int(num2), int(num1/num2)))
# except ValueError as err:
#     print("Value Error 0}".format(err))
# except BigNumError as err:
#     print("Error! 한자리 숫자 입력")
#     print(err)
# finally:
#     print("End")


chicken = 10
waiting = 1
while(True):
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨 ?"))
    
    if order > chicken:
        print("재료 부족")
    else:
        print("[대기번호 {0}] {1} 마리".format(waiting, order))
        waiting += 1
        chicken -= order