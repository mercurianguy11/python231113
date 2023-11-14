# Pserson2.py

# 부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, PhoneNumber:{1})".format(self.name, self.phoneNumber))
    def working(self):
        print("현재 작업중....")
    def coding(self):
        print("현재 코딩중....")

# Person class를 상속받아 Student class 정의
# 자식 클래스 정의
class Student(Person):
    # 멤버변수 추가 (덥어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        
        # self.name = name
        # self.phoneNumber = phoneNumber
        #명시적으로 부모 생성자 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    # 상속받아서 덮어쓰기 (재정의, override)
    def printInfo(self):
        print("Info(Name:{0}, PhoneNumber:{1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID:{1})".format(self.subject, self.studentID))


p1 = Person("전우치", "010-222-1234")
print(p1.__dict__)
s1 = Student("이순신","010-111-1234", "빅데이터학과", "201234")
print(s1.__dict__)

p1.printInfo()
s1.printInfo()
s1.working()
s1.coding()

