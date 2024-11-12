numbers = [1, 2, 3, 4, 5]

iter_numbers = iter(numbers)
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.data):
            result = self.data[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator([1,2,3,4])

for i in my_iter:
    print(i)