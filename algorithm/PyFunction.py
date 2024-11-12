def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Alice', age=25, city='New York')

square = lambda x: x ** 2
print(square(5))