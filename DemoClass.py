# DemoClass.py

# 함수(3장) : 1개 기능
# 클래스(4장) : N개 변수 + N개 함수
# 모듈&패키지 : 1개 파일, N개 파일(폴더)

# Cpython 수백개 클래스 제공
# 직원 클래스 : 사번, 이름, 부서코드 등의 데이터가 필요하고 입사 퇴사와 같은 액션이 필요
#,제품 클래스 작성 : 제품번호, 제품명, 설명, 분류코드등이 필요하고 제품등록, 수정, 삭제와 조회등의 액션이 필요. 

# CRUD : create, read, update, delete

# 객체지향프로그래밍의 3가지 특징 (OOP: objected oriented programing)
# 1. 추상성 : 꼭 필요한 부분만 구현하는 것
# 2. 상속성 : 부모 클래스에서 공통 부분을 상속 받는 것
# 3. 다형성 : 동일한 인터페이스에 대해 구체적인 인스턴스마다 다른 동작을 할 수도 있는 것

# 1. 클래스(Class) 정의 : ex) 쿠키틀, 붕어빵틀 - 템플릿, 원본, 청사진
# 2. 객체(Object, Instance) : 실제 메모리에서 실행, 복사본..
# 3. 메소드(Method) 호출

# 레고 블럭처럼 조립을 통한 개발이 가능하다.
# Class는 Type 을 정의
# 멤버변수와 멤버함수(메소드)를 정의

# Instance 는 복사본을 만든다.
# class 클래스명(상위 클래스):
#       def 함수명(self, 인자1, 인자2, ...):
#            statement1
#            statement2
#            return

# 부모 클래스 : Person
# 자식 클래스 : Manager, Employee, Alba, etc...

# Pserson1 Class
class Person1:
    # object 부모 클래스에서 정의된 함수, 생성자 (Constructor), self 는 복사본(자기자신) - 첫번째 인자 예약(내꺼...)
    # java, C# : this, self, super, base ?
    def __init__(self):  
        self.name = "default name"
    def print(self):
        print("Person1 : My name is {0}".format(self.name))
    def getName(self):
        print("Person1 : getName() is returned {0}".format(self.name))
        return self.name
    def setName(self, new_name):
        print("Person1 : setName({0})".format(new_name))
        self.name = new_name

# p1 인스턴스 정의
p1 = Person1()

# 메소드 호출
p1.print()
p1.name = "Jack"
print(p1.getName())
p1.print()
print("\n")
p1.setName("Jerry")
p1.print()
print("\n")

p3 = Person1()
p3.print()
p3.name="전우치"
p3.print()
print("\n")
print("---- create Person2 class -------")
class Person2:
    def __init__(self, name):
        self.name = name
    def print(self):
        print("Person2 : My name is {0}".format(self.name))

p2 = Person2("Tom")
p2.print()

# 런타임(코드가 실행중)
Person1.title = "new title"
print(p1.title)    # 인스턴스를 뒤졌는데 title이 없다. 클래스를 뒤진다. 전역변수를 뒤진다
print(p3.title)    # 자동완성이 안뜨면 가급적 사용 자제.... 클래스 정의 후 추가 작성 가능성 많음... 에러 표시 안함..
print(Person1.title)
