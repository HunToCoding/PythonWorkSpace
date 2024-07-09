# import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "농구", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file의 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# Close가 필요 없는 방법
# with open("profile.pickle", "rb") as profile_file:
    # print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf-8") as study_file:
    # study_file.write("파이썬 공부 중")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())


# Quiz 1년치 보고서 만들기

# for num in range(1, 51):
    # with open(str(num)+"주차.txt", "w", encoding="utf8") as Weekend:
    #    Weekend.write("- {0} 주차 주간보고 -".format(num)) 
    #    Weekend.write("\n부서 : ") 
    #    Weekend.write("\n이름 : ") 
    #    Weekend.write("\n업무 요약 : ") 

