# if, for, switch 등

# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or "눈":
#     print("우산을 챙기세요")

# elif weather == "미세먼지":
#     print("마스크를 챙기세요")

# else :
#     print("준비물 필요 없어요")

# temp =  int(input("기온은 어때요? "))

# if 30 <= temp :
#     print("너무 더우니 나가지 마세요")
# elif 10 <= temp and temp < 30 :
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10 :
#     print("외투를 챙기세요")
# else :
#     print("추우니 건강 조심하세요")

# 반복문 for, while
## for문

# for waiting_No in [0, 1, 2, 3, 4 ,5]:
#     print("대기번호 : {0}".format(waiting_No))

# for waiting_No in range(1, 6) : # 1시작 6-1까지 
#     print("대기번호 : {0}".format(waiting_No))

# starbuks = ["아이언맨", "토르", "캡틴아메리카", "헐크"]

# for customer in starbuks :
#     print("{0}, 커피가 준비되었습니다".format(customer))

## while 문

# customer = "토르"
# index = 5

# while index >= 1 :
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1;
#     if index == 0:
#         print("커피가 폐기 되었습니다.")

# customer = "토르"
# person = "unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("성함이요? ")

## continue, break

# absent = [2, 5] # 결석
# no_book =[7]    # 책 잊음
# for student in range(1, 11) :
#     if student in absent :
#         continue
#     elif student in no_book :
#         print("오늘 수업끝, {0}는 교무실로".format(student))
#         break
    
#     print("{0}, 책 읽어보자".format(student))

# 출석 번호 1~4 앞에 100을 붙이기로 바뀜
# student = [1, 2, 3, 4, 5]

# student = [ i + 100 for i in student]
# print(student)

# student_name = ["Iron Man", "Thor", "Captin"]
# student_name = [len(i) for i in student_name]
# print(student_name)

# student_name = ["Iron Man", "Thor", "Captin"]
# student_name = [i.upper()  for i in student_name]
# print(student_name)

# Quiz
from random import *
count = 0
for i in range(1, 51): # 1~ 50
    time = randrange(5, 51) # 5 ~ 50 

    if 5 <= time <= 15 : # 5~ 15분 이내 손님 탑승 승객 수 증가
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 수 : {0}".format(count))
