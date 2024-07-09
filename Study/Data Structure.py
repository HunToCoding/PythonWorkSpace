# # 자료구조 변경
# # 음료수  종류
# menu = {"Coffee", "Milk", "Juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# Quiz

# 1. 편의상 댓글은 20명, 아이디는 1~20
# 2. 댓글 내용과 상관 X, 무작위 추첨 중복 X
# 3. random 모듈의 shuffle과 sample 활용

# Example 
# -- 당첨자 발표 --
# 치킨 : 1
# 커피 : [2, 3, 4]
# -- 축하합니다. -- 

# 활용 예제
# from random import *
# list = [1, 2,3, 4, 5]
# shuffle(list)
# print(sample(list, 1))

from random import *
# list 20~
# 첫 번째 (무식한) 방식 user = [1, 2, 3, 4, ..~] 
users = range(1, 21) # 1~20 까지 숫자 생성
users = list(users)
# print(users, type(users))

shuffle(users)
winner = sample(users, 4)

print( "-- 당첨자 발표 -- ")
print(" 치킨 당첨 : {0}".format(winner[0]))
print(" 커피 당첨 : {0}".format(winner[1:]))
print( "-- 축하합니다. -- ")

