# BankAccount.py

# object.__init__(self[, ...]) : 클래스 메소드, 생성자
# object.__del__(self) : 클래스 메소드, 소멸자
# object.__add__(self, other) : 클래스 메소드, +
# object.__sub__(self, other) : 클래스 메소드, -
# object.__mul__(self, other) : 클래스 메소드, *
# object.__div__(self, other) : 클래스 메소드, /
# object.__truediv__(self, other) : 클래스 메소드, __future__ 모듈의 division 이 실행 되었을 때 / 연산자가 실행
# 됨
# object.__floordiv__(self, other) : 클래스 메소드, //
# object.__mod__(self, other) : 클래스 메소드, %
# object.__divmod__(self, other) : 클래스 메소드, divmod()
# object.__pow__(self, other[, modulo]) : 클래스 메소드, pow(), **
# object.__lshift__(self, other) : 클래스 메소드, <<
# object.__rshift__(self, other) : 클래스 메소드, >>
# object.__and__(self, other) : 클래스 메소드, &
# object.__xor__(self, other) : 클래스 메소드, ^
# object.__or__(self, other) : 클래스 메소드, |
# ###피연산자가 바뀐 경우에는 위 메소드에다가 r 을 앞에다가 붙이면 됨.###
# ###확장 산술 연산자(+=, -= 과 같은)는 위 메소드에다가 i 를 붙이면 됨. 단, divmod 는 확장 산술 연사자가 없음.###
# object.__neg__(self) : 클래스 메소드, - (단항 연산자)
# object.__pos__(self) : 클래스 메소드, + (단항 연산자)
# object.__abs__(self) : 클래스 메소드, abs()
# object.__invert__(self) : 클래스 메소드, ~ 비트 반전.
# object.__complex__(self) : 클래스 메소드, complex(), 리턴 값은 반드시 복소수값
# object.__int__(self) : 클래스 메소드, int(), 리턴 값은 반드시 정수형
# object.__long__(self) : 클래스 메소드, long(), 리턴값은 반드시 Long 형
# object.__float__(self) : 클래스 메소드, float(), 리턴값은 반드시 실수형
# object.__oct__(self) : 클래스 메소드, oct(), 리턴값은 반드시 문자열
# object.__hex__(self) : 클래스 메소드, hex(), 리턴값은 반드시 문자열
# object.__coerce__(self, other) : 클래스 메소드, 반드시 일반적인 수 타입으로 변환될 수 있는 self, other 을 포함하
# 는 튜플을 리턴하거나 변환될 수 없을 경우 None 객체를 리턴해야 한다. 튜플의 값들이 내장된 연산이 적용될 수 있을 경우
# 다른 연산자 메소드보다 우선적으로 호출됨.(자세한 것은 파이썬 문서 참조.)
# object.__len__(self) : 클래스 메소드, len(), 반드시 0 이상의 정수형을 리턴해야 함.
# object.__contains__(self, item) : 클래스 메소드, in 연산자.
# object.__getitem__(self, key) : 클래스 메소드, self[key]
# object.__setitem__(self, key, value) : 클래스 메소드, self[key] = value
# object.__delitem__(self, key) : 클래스 메소드, del self[key]
# object.__iter__(self) : 클래스 메소드, 반복자를 요구할 때 호출됨.
# ###shelve 모듈을 이용하여 사전과 같은 방식으로 파일을 입,출력할 수 있다.###
# object.__repr__(self) : 클래스 메소드, repr(), ` `, __str__ 메소드가 정의되어 있지 않다면 대신 호출됨. 리턴값은
# 반드시 문자열이어야 함.
# object.__str__(self) : 클래스 메소드, str(), print, __repr__ 메소드가 정의되어 있지 않더라도 호출되지 않음. 리턴
# 값은 반드시 문자열이어야 함.
# object.__cmp__(self, other) : 클래스 메소드, self < other 일 경우 음의 정수, self == other 일 경우 0, self >
# other 일 경우 양의 정수 리턴. 메소드가 정의되어 있지 않다면 객체의 '주소'로 비교를 함.
# object.__lt__(self, other) : 클래스 메소드, self < other
# object.__le__(self, other) : 클래스 메소드, self <= other
# object.__eq__(self, other) : 클래스 메소드, self > other
# object.__ne__(self, other) : 클래스 메소드, self >= other
# object.__gt__(self, other) : 클래스 메소드, self == other
# object.__ge__(self, other) : 클래스 메소드, self != other
# ### 위 비교함수가 cmp 보다 우선됨. ###
# object.__hash__(self) : 클래스 메소드, 클래스 객체를 사전의 키로 이용할 때 필요. 이때 __cmp__ 나 __eq__ 메소드도
# 정의되야 함. 그리고 리턴값은 반드시 정수형이여야 함.
# object.__nonzero__(self) : 클래스 메소드, bool(), 진리값(0, 1 포함)을 리턴해야 함. 메소드가 정의되어 있지 않으면
# __len__ 메소드를 호출하고 이때 결과가 0이 아니면 True 를 리턴함. __len__도 정의되어 있지 않으면 True 를 리턴.
# object.__getattr__(self, name) : 클래스 메소드, 정의되어 있지 않은 속성을 참조할 때 호출됨(위임 기법에서 사용됨).
# name 은 문자열이며 호출한 속성의 이름을 가짐.
# object.__getattribute__(self, name) : 클래스 메소드, __getattr__ 과 같으나 속성이 정의되어 있어도 호출됨. 그리
# 고 이 메소드를 사용하는 클래스는 object 클래스를 상속해야 함. 또, object.__getattribute__(self, name) 으로 사용
# 해서 값을 리턴해야 한다.
# object.__setattr__(self, name, value) : 클래스 메소드, self.name = value 와 같이 속성에 치환(대입)이 일어날 때
# 호출됨. 그리고 치환(대입)은 일어나지 않으므로 이 메소드에서 다시 치환(대입) 시켜야함(단, 클래스 인스턴스의 사전
# (__dict__)에 값을 저장시키는 방식이어야 함.)
# object.__delattr__(self, name) : 클래스 메소드, del self.name 시에 호출됨. 그리고 삭제는 일어나지 않으므로 이
# 메소드에서 다시 삭제 시켜야함(단, 클래스 인스턴스의 사전 값을 없애는 방식이어야 함.)
# object.__call__(self[, args...]) : 클래스 메소드, 함수처럼 호출할 수 있게 함.
# callable(object) : 내장 함수, 객체가 호출 가능한지 알아봄.


# 변수 앞에 __을 붙여서 변수를 은폐할수 있음 -> 외부 접근 불가능???
class BankAccount2:
    # 초기화
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance
        # print("BankAccount Instance is created!")
    #입금
    def deposit(self, amount):
        self.balance += amount
    #출금
    def withdraw(self, amount):
        self.balance -= amount
    #결과를 문자열로 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, \
                                        self.name, self.balance)
    def __del__(self):
         print("BankAccount2 Instance is deleted!")
    
# 인스턴스 객체를 생성
account1 = BankAccount2(100, "장보고", 15000)
print(account1)
account1.deposit(5000)
print(account1)
account1.withdraw(3000)
account1.balance = 150000000
print(account1)


# 변수 앞에 __을 붙여서 변수를 은폐할수 있음 -> 외부 접근 불가능???
class BankAccount:
    # 초기화
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance
        # print("BankAccount Instance is created!")
    #입금
    def deposit(self, amount):
        self.__balance += amount
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #결과를 문자열로 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
                                        self.__name, self.__balance)
    def __del__(self):
         print("BankAccount Instance is deleted!")
    

# 인스턴스 객체를 생성
account2 = BankAccount(100, "전우치", 15000)
print(account2)
account2.deposit(5000)
print(account2)
account2.withdraw(3000)

# 적용 안됨...
account2.__balance = 150000000
print(account2)

## 보안에 취약......
print(account2._BankAccount__balance)  
account2._BankAccount__balance = 150000000   
print(account2)

print ("\n----- 전체 코드 실행 종료--------")

# 플라이트시뮬레이터 2024