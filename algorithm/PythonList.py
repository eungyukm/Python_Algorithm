string_list = ["a", "b", "c", "d"]
number_list = [1, 2, 3, 4, 5]

# 인덱싱
print(string_list[0]) # a
print(number_list[2]) # 3

# 슬라이싱
print(string_list[:2])  # ['a', 'b']
print(number_list[1:3]) # [2, 3]

# 더하기
print(string_list + number_list) # ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5]

# 반복하기
print(string_list * 2) # ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']

# 길이 구하기
print(len(number_list)) # 5

# 요소 추가
number_list.append(0)
print(number_list)  # [1, 2, 3, 4, 5, 0]

# 리스트 정렬
number_list.sort()
print(number_list)  # [0, 1, 2, 3, 4, 5]

# 리스트 역순
number_list.reverse()
print(number_list)  # [5, 4, 3, 2, 1, 0]

# 리스트 요소 제거
number_list.remove(5)
print(number_list)  # [4, 3, 1, 0]

# 리스트 요소 개수 세기
print(number_list.count(4)) # 1

# 리스트 확장
number_list.extend([5, 6, 7])
print(number_list)  # [4, 3, 1, 0, 5, 6, 7]