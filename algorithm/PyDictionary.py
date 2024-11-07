dictionary = {
    "name": "John",
    "age": 30,
    "gender": "남"
}

print(dictionary["name"]) # John

# key value 추가, 삭제
print(dictionary["age"])

del dictionary["gender"]
print(dictionary) # {'name': 'John', 'age': 30}

# key value 추가
dictionary["hp"] = 100
print(dictionary) # {'name': 'John', 'age': 30, 'hp': 100}

# key 값만 모아 dict_key 객체를 리턴합니다.
print(dictionary.keys()) # dict_keys(['name', 'age', 'hp'])

# value 값을 모아 dict_values 객체
print(dictionary.items()) # dict_items([('name', 'John'), ('age', 30), ('hp', 100)])

print(dictionary.get("name")) # John

# Dictionary Clear
dictionary.clear()
print(dictionary) # {}