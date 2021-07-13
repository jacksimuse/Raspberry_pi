class Person(object):
    total = 0

    def __init__(self, name, age): #기본 생성자(self) / 오버로딩
        self.name = name
        self.age = age

    def getAgte(self):
        return self.age

class Man(Person): # 클래스 상속
    gender = 'male'

class Korean(Person):
    nationality = 'korea'

class KoreanMan(Man, Korean):   # 다중상속
    pass
