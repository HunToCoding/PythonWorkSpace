# 지역 변수, 전역 변수

# gun = 10

# def checkpoint(soldiers):
#     global gun               #  전역 공간에 있는 gun 사용하겠다는 의미
#     gun = gun - soldiers     # Error 지역변수 초기화 안하고 사용
#     print("[함수] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers) :
#     gun = gun - soldiers
#     print("[함수] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz func

# 표준 체중 구하는 함수 작성
# 남성 : 키 * 키 * 22
# 여성 : 키 * 키 * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력 예시 : 키 175cm 남자의 표준 체중은 67.38kg

def MyFunc(height, gender):
    
    if gender == "남자" :
        return height * height * 22
    else:
        return height * height * 21

mheight = 175
mgender = "남자"

fheight = 162
fgender = "여자"

male_result = round(MyFunc(mheight / 100, mgender), 2)
female_result = round(MyFunc(fheight / 100, fgender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".\
      format(mheight, mgender, male_result))

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".\
      format(fheight, fgender, female_result))