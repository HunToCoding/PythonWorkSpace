# 예외 처리

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자 입력 : ")))
#     nums.append(int(input("두 번째 숫자 입력 : ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# except ValueError:
#     print("Error!")

# except ZeroDivisionError as err:
#     print(err)

# except IndexError as err:
#     print(err)

# except Exception as err:
#     print("UnKnown Error {0]".format(err))

# 사용자 정의 Error 처리
class BigNumError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기")
    num1 = int(input("1 입력 : "))
    num2 = int(input("2 입력 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumError("입력 값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(int(num1), int(num2), int(num1/num2)))
except ValueError as err:
    print("Value Error 0}".format(err))
except BigNumError as err:
    print("Error! 한자리 숫자 입력")
    print(err)

