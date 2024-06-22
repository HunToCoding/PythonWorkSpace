

# http://naver.com
url = "http://naver.com"
url = "http://google.com"


string = url.replace("http://", "")
string = string[:string.index(".")]

password = string[:3] + str(len(string)) + str(string.count("e")) + "!"

print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
