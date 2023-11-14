# ChatGPT_Person.py


# ChatGPT 질문 :   

# 파이썬에서 Person클래스는 멤버변수로 id, title을 가지고 있고 
# Person 클래스를 상속받은 Manager 클래스는 skill변수가 추가되어 있고 
# printInfo()메서드로 변수값을 출력해야되. 
# Person 클래스를 상속받은 Employee클래스는 role변수가 추가됨. 
# 해당 클래스 코드를 생성해서 테스트하는 샘플코드를 10개 추가해줘. 주석도 달아줘

class Person:
    def __init__(self, _id, title):
        """사람(Person)을 나타내는 클래스입니다."""
        self.id = _id
        self.title = title

    def printInfo(self):
        """사람의 정보를 출력하는 메서드입니다."""
        print(f"이 사람은 - ID: {self.id}, 이름: {self.title}")


class Manager(Person):
    def __init__(self, _id, title, skill):
        """매니저를 나타내는 클래스입니다. 사람(Person) 클래스를 상속받습니다."""
        super().__init__(_id, title)
        self.skill = skill

    def printInfo(self):
        """매니저의 정보를 출력하는 메서드입니다."""
        super().printInfo()
        print(f"매니저의 기술은: {self.skill}")


class Employee(Person):
    def __init__(self, _id, title, role):
        """직원(Employee)을 나타내는 클래스입니다. 사람(Person) 클래스를 상속받습니다."""
        super().__init__(_id, title)
        self.role = role

    def printInfo(self):
        """직원의 정보를 출력하는 메서드입니다."""
        super().printInfo()
        print(f"직원의 역할은: {self.role}")


# 테스트를 위한 샘플 코드
# Person, Manager, Employee 클래스의 인스턴스를 생성하고 printInfo() 메서드 호출

# Test 1
person1 = Person(1, "존 도우")
person1.printInfo()

# Test 2
manager1 = Manager(2, "제인 매니저", "리더십")
manager1.printInfo()

# Test 3
employee1 = Employee(3, "앨리스 직원", "개발자")
employee1.printInfo()

# Test 4
person2 = Person(4, "밥 스미스")
person2.printInfo()

# Test 5
manager2 = Manager(5, "마이크 매니저", "커뮤니케이션")
manager2.printInfo()

# Test 6
employee2 = Employee(6, "캐롤 직원", "디자이너")
employee2.printInfo()

# Test 7
person3 = Person(7, "에바 존슨")
person3.printInfo()

# Test 8
manager3 = Manager(8, "톰 매니저", "프로젝트 매니지먼트")
manager3.printInfo()

# Test 9
employee3 = Employee(9, "크리스 직원", "테스터")
employee3.printInfo()

# Test 10
person4 = Person(10, "그레이스 리")
person4.printInfo()

# added by me
p1 = Person(100, "개발자")
p1.printInfo()

# 챗GPT 사용설명서