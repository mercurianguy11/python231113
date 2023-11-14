# Person.py

# 함수(LGB local Global Built-in 순)
# 클래스 참조 순서 : 인스턴스 객체 영역 -> 클랙스 객체영역 -> 전역 영역(전역변수)

# 디자인 타임(VB, 델파이) : 코딩중~~~
# 런타임 : 실행중~~~
# IDLE 
# VS Code 

# 파이썬에서는 런타임에 각 클래스와 인스턴스 이름공간에 멤버 변수를 추가하거나 삭제할 수 있다.

# *컴파일러: C, C++, C#, VB
# 소스코드(사람이 작성)--------------------> 기계어 코드 
# *.c, *.vb                  (빌드, 컴파일, 만들기) Person.exe 

# 번역이 끝나면 한글판 보기(정적인 형식) -> 타입을 확장할수 없다...

# *인터프리터:R, Python, JavaScript (스크립트언어, 간이언어) - 실행파일을 만들지 않는다. 
# 소스코드(사람이 작성)  ----------------> 인터프리팅(라인단위로 해석하고 실행)
# *.py 

# 동적인 형식(필요하면 확장) -> 동적으로 확장 가능하다. ex) class 에 title 멤버변수 생성 & 추가
# 파이썬이 문법이 너무 느슨하다(자유로운 언어) : 조심하게 사용해야한다.
import sys

# Pserson1 Class
class Person:
    # object 부모 클래스에서 정의된 함수, 생성자 (Constructor), self 는 복사본(자기자신) - 첫번째 인자 예약(내꺼...)
    # java, C# : this, self, super, base ?
    def __init__(self):  
        self.name = "default name"
    def print(self):
        print("Person1 : My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
Person.title = "New title"
print(p1.title)
print(p2.title)
print(Person.title)


str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = ""  # 인스턴스 멤버변수
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str) # self.str 이 아니기때문에, 전역변수 str로 인식... 이름 충돌...
        print(self.str) # 안정하게 코딩해야한다.... self.... 붙여라

print("\n")
g = GString()
g.set("First Message")
g.print()

# python 2.7 -> 객체지향 언어 다소 약함
# python 3.* -> 객체지향 언어 O : 모든 클래스는 Object 클래스를 상속 받는다......(Object 클래스가 근본)
# __init__(), __del__(), __str__() 함수 이름을 기억해라..
# GC (Garbage Collection, 가비지 컬렉션) : 쓰레기 정리...수거..
# java VM (virtual machine)
# c#, VB CLR(Common Language RunTime)
# python 인터프리터 

print(sys.getrefcount(g))
del g
# print(sys.getrefcount(g))


class MyClass:
     def __init__(self, name, age):
         self.name = name
         self.age = age
         print("MyClass Instance is created! value = %s, age = %d" %(name,age))
     def __str__(self):
         return "{0}:{1}".format(self.name, self.age)
     def __del__(self):
         print("MyClass Instance is deleted!")
     
m = MyClass("YJ",39)
# print(m.__str__())
print(m)
del m
print ("\n----- 전체 코드 실행 종료--------")