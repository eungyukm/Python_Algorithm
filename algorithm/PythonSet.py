# Python set은 고유한 값들로 이루어진 순서가 없는(collection) 데이터 타입입니다.
fruits = {"apple", "banana", "cherry"}
print(fruits)

set1 = set([1,2,3,4,5,6])
set2 = set([3,4,5,6,7,8])

# 교집합
print(set1 & set2) # {3, 4, 5, 6}

# 합집합
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8}

# 차집합
print(set1 - set2) # {1, 2}

# 요소 추가
set1.add(11)
print(set1) # {1, 2, 3, 4, 5, 6, 11}

# 요소 여러개 추가
set1.update([12, 13, 14])
print(set1) # {1, 2, 3, 4, 5, 6, 11, 12, 13, 14}

# 특정 요소 제거
set1.remove(11)
print(set1) # {1, 2, 3, 4, 5, 6, 12, 13, 14}

# 중복제거
dup = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, ]
print(set(dup)) # {1, 2, 3, 4}