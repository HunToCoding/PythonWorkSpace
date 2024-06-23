# 기본값
# def  profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1} 이며, 주 언어 : {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 가정 :  같은 학교 같은 학년 같은 수업
# 이럴 때 사용되는 것이 기본 값

def profile(name, age = 17, main_lang="Pyhton") :
    print("이름 : {0}\t 나이 : {1} 이며, 주 언어 : {2}"\
           .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")