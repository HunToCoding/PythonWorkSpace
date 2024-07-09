# sep 를 이용한 문자열 출력
# end 출력의 끝 부분을 설정 된 문자열로 바꾸는 것
# print("Pytoh", "JAVA", sep=", ") #, end="?")
# print("무엇이 더 재미있을까요?")

# import sys
# print("Pytoh", "JAVA", file=sys.stdout)
# print("Pytoh", "JAVA", file=sys.stderr)

# 시험 성적
# score = {"수학":0, "영어":50, "코딩":100}
# for subject, score in score.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기 순번 표
# # 001, 002, 003, 004등의 형식 zfill(nCount) #nCout = 3 (세자리 숫자)
# for num in range(1, 21):
#     print("대기번호 : "+ str(num).zfill(3))

# 사용자 입력을 받으면 항상 str Type
answer = input("아무 값 입력 : ")
print(type(answer))
# print("입력 값 : " + answer)
