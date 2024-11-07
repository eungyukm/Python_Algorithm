# 조건문 (if else)
from nis import match

age = 25
has_license = True
if age >= 18 and has_license:
    print("운전 가능합니다.")

# 숫자 입력 예제
number = int(input("숫자를 입력하세요: "))
if number > 0:
    print("양수입니다.")
elif number == 0:
    print("0입니다.")
else:
    print("음수입니다.")

# 로그인 시스템
username = "admin"
password = "1234"

input_username = input("사용자 이름: ")
input_password = input("비밀번호: ")

if input_username == username and input_password == password:
    print("로그인 성공")
else:
    print("로그인 실패")