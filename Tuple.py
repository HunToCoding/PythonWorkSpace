
menu = ("돈까스", "치즈까스", "제육볶음")

print(menu[0]) 
print(menu[1]) 

# 투플(Tuple) 값 변경 불가

name = "김종국"
age = 20
hobby = "Coding"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "Coding")
print(name, age,  hobby)

# Set 세트 = 집합
#  중복 X, 순서 X,

my_set = {1, 2, 3, 3, 3, 65, 151 }
print(my_set)

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "박명수"])

# 교집합 출력 (JAVA, Python 모두 할 수 있는 사람)

print(java & python)
print(java.intersection(python))

# 합집합 (java or python도 할 수 있는 개발자)
print(java or python)
print(java | python)
print(java.union(python))

# 차 집합
print(java - python)
print(java.difference(python))

# Python 할 줄 아는 사람 추가
python.add("김태호")

print(python)

# JAVA 할 줄 모름
java.remove("김태호")

print(java)






