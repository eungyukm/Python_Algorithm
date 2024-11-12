class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def __add__(self, other):
        return self.age + other.age

    def __eq__(self, other):
        return self.age == other.age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

kim = human('Kim', 29)
print(kim.name)
print(kim.age)
park = human('Park', 35)
print(park.name)
print(park.age)

print(kim + park)
print(kim == park)
print(kim)