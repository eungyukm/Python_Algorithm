count = 0
while True:
    print(count) # 0, 1, 2, 3, 4
    count += 1

    if count == 5:
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) # apple, banana, cherry

person = {"name": "Alice", "age": 25}
for key in person:
    print(key, person[key]) # name Alice, age 25