# fuction3.py
import test  # test.py 파일 import
# python은 모든것이 객체 -> function, int, string, etc...
# 코드 재사용(함수-> 모듈(파일))
def times(a,b):   # python 은 return 형 명시 없음 -> 도움말 주석 필요
    return a*b

print(times)
print(times(5,6))


# test.py에 작성된 calc 함수 참조
print(test.calc(7,2))

print(globals())

#전역변수 x
x=1   
print("####### 전역변수:",x)
print(x)
# return 연습
def setValue(newValue):
    x=newValue  # 지역변수 x
    print("####### 지역변수:",x)
setValue(100)
retValue=setValue(5)
print(retValue)  # None is NULL....

def getValue():
    return x
print("------test 1111------")
print(getValue())
print("------test 2222------")
x=10
print(getValue())
print("------test 3333------")

print(x)

def swap(x,y):
    return y,x
result = swap(3,4)
print(result)

# python namespace:global  전역변수 x
# python namespace:func    지역변수 x
# 파이썬 우선순위  LGB -> Local, Global, Built-in 


print("----- 지역변수와 전역변수----")
x=5
def func(a):
    print("## func : input value a =",a, "전역변수 x =",x)
    return a+x  # 함수 내부에 해당 이름이 없기에 전역 영역에서 찾아서 return 
print(func(1))

def func2(a):
    x=2
    print("## func2 : input value a = %d, 지역변수 x = %d" % (a,x))
    return a+x  # 함수 내부에 x라는 이름이 등록됨, 지역변수를 사용하여 return
print(func2(1))

def time(a=10, b=20):
    print("## time : input value a = %d, b = %d" % (a,b))
    return a*b

#print(times())  # error
#print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL = "http://" + server + ":" +port
    return strURL
print(connectURI("naver.com","80"))
print(connectURI(port="8080", server="daum.net"))

def union(*ar):
    result=[]
    for item in ar:
        print("## union : item = %s" % item)
        for x in item:
            print("## union : x = %s" % x)
            if x not in result:
                print("## union : append - %s" % x)
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

# 문법 -> lambda  인자 : <구문>
g=lambda x,y:x*y   # lambda 익명함수 : 일회성, 즉흥적 -> 한줄 코딩 (g 변수에 흔적을 남김)
print(g(2,3))
print((lambda x:x*x)(3)) # 함수정의 후 바로 호출 -> 흔적이 없다.

print(globals())




