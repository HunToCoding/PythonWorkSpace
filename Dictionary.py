# Dictionaryasd

# variable = [ket : value]
cabinet = {3 : "유재석", 100 : "김태호"}

# 출력 법
print(cabinet[3])
print(cabinet[100])

# 또 다른 방법
print(cabinet.get(3))

#  Error
# print(cabinet[5])
# But! 우 히히히히히히히ㅣ히히히히히히힣
print(cabinet.get(5), "사용가능")
print("it's Not! Erorr!")

# 나중에 사물인식, AI 할거야
# 백엔드도 해보고 싶어어어ㅓ어어어어어어어어어 ㅓ리눅스 좋아ㅏㅏㅏㅏ

# Dictionary에 값이 있는지 확인 법
print(3 in   cabinet) # True
print(5 in   cabinet) # Flase

Box = {"a-3": "유재석", "B-100":"김태호"}
print(Box["a-3"])
print(Box["B-100"])

# New Value
Box["a-3"] = "김종국"
Box["C-20"] = "조세호"
print(Box)

# Delete Value
del Box["a-3"]
print(Box)

# Total Key, Value
print(Box.keys())
print(Box.values())

# Total Print
print(Box.items())

# Clear
Box.clear()
cabinet.clear()

print(Box, cabinet)
