hi = "안녕"
more_politely = ("하세요")

print(hi + more_politely) # 안녕하세요
print(hi * 3) # 안녕안녕안녕

# 문자열의 길이
print(len(hi))

# 문자열의 인덱싱과 슬라이싱
print(hi[0]) # 안
print(hi[1]) # 녕
print(more_politely[:2]) # 하세요
print(more_politely[2]) # 요

# 문자열의 포맷팅
age = 10
print("%s%s, 저는 김은규입니다" %(hi, more_politely)) # 안녕하세요 김은규입니다
print("제 나이는 %d살 입니다" %age) # 제 나이는 10살 입니다

# format 함수를 이용한 포멧팅
print("{0}{1}, 저는 김은규입니다.".format(hi, more_politely))

# f-string
print(f"{hi}{more_politely}, 저는 김은규입니다.") # 안녕하세요, 저는 김은규입니다.

# 소수점 표현 f-string
pi = 3.1415926535

# f"{실수:몇번째자리까지}
print(f"{pi:0.2f}") # 3.14
print(f"{pi:0.4f}") # 3.1416

# 문자열 관련 함수들
string = "python is easy programming language"

# 개수 세기
print(string.count("a")) # 2

# 위치 찾기
print(string.find("e"))  # 5
print(string.find("b"))  # 찾는 문자가 여러개라면 가장 첫번째자리를 반환합니다.
print(string.find("z"))  # 찾는 문자가 없다면 -1을 반환합니다.

# index라는 함수도 위치를 찾는데 사용되나
# ValueError: substring not found
# print(string.index("z"))

# 문자열 삽입
print(".".join(string))

# 대문자 소문자 변환
print(string.upper()) # PYTHON IS EASY PROGRAMMING LANGUAGE
print(string.lower()) # python is easy programming language

blank_string = "   blank string    "

# 오른쪽 공백 지우기
print(blank_string.rstrip()) # blank string
# 왼쪽 공백 지우기
print(blank_string.lstrip()) # blank string
