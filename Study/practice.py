
#  출력, 자료형 등 건너뜀..
# 사실 날림... 개같은거;;
#  List [] Study

# 지하철 칸 별로 10, 20, 30 명이 있음

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇명 있는지?

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬
# num_list = [5, 2, 45, 1,2, 345]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# 다양한 자료형 사용 가능

num_list = [1, 2, 3, 65, 17,18, 8,222, 301]
mix_list = ["조세호", 20, True]
#print(mix_list)

# list 확장
num_list.extend(mix_list)

print(num_list)
