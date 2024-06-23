# 키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(name="김태호", age=25,main_lang="자바")

# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5);

def profile(name, age, *langague):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end = " ")
    for lang in langague:
        print(lang+"\t", end = " ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#", "javascript")
profile("김태호", 25, "Kotlin", "Switf")
profile("조세호", 19, "java", "Switf")