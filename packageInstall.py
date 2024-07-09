# pip install packageName

# 내장 함수
# input : 사용자 입력 받는 함수
# lan = input("언어 : ")
# print("{0} ~".format(lan))

# dir : 객체를 넘겨줬을 때, 그 객체의 변수, 함수 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "jim"
# print(dir(name))

# 외장 함수
# glob : 경로 내의 폴더 / 파일 목록 조회
# import glob as gl
# print(gl.glob("*.py"))

# os : 운영 체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재")
#     os.rmdir(folder)
#     print(folder, "폴더 삭제")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더 생성")
# print(os.listdir())

# time : 시간
# import time as ti
# print(ti.localtime())
# print(ti.strftime("%y-%m-%d %H:%M:%S"))

# DateTime
# import datetime as dt
# # print("오늘 날짜 ", dt.date.today())

# today = dt.date.today() # 오늘 날짜 저장
# td = dt.timedelta(days=100) # 100일 뒤
# print("100일 후 는", today+td)