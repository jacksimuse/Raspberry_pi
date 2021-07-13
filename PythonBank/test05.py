import time
import Person
# 클래스 객체

number = [10, 20, 30]
print(dir(number))

p = Person.Person('Sung', 44)
print(p.age)
print(p.name)
print(p.getAgte())
print(p.total)

john = Person.Person("John Doe", 36)
print(john.name)