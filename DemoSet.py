# DemoSet.py

a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(type(a))
print(a.union(b))  # 합집합
print(a.intersection(b))  # 교집합
print(a.difference(b)) # 차집합

t=(1,2,3)
print(type(t))

device=("아이폰", "아이패드", "노트북")
def calc(a,b):   # 함수 정의
    return a+b, a*b  # tuple type return
result = calc(5,6)
print(result)

print(device.count("아이폰"))

print("id: %s, name: %s" %("kim", "김유신"))
args=(4,5)
print(calc(*args))


# type casting   list, int, str, range?
a = set((1,2,3))
print(a)
print(type(a))
b=list(a)
print(b)
print(type(b))
c=tuple(b)
print(c)
print(type(c))


print("--------- set형식 ---------")
a = {1, 2, 3, 3}
b = {3, 4, 4, 5}
print(a)
print(type(a))
print(a.union(b))  # 합집합
print(a.intersection(b))  # 교집합
print(a.difference(b)) # 차집합

print("--------- tuple형식 ---------")
tp=(10, 20, 30)
print(len(tp))
print(type(tp))

#함수 정의
print("--------- calc2 function define ---------")
def calc2(a,b):
    return a+b, a*b
print(a)
print(b)

#호출
result = calc2(3,4)
print(result)
print("id:%s, name:%s" % ("kim", "김유신"))
args=(5,6)
print(calc2(*args)) # '*' <== tuple 인자를 알려주는 식별자


# 선택한 블럭을 주석처리 : ctrl + /

print("--------- 형식변환 ---------")
q=set((1,2,3))
print(q)
print(type(q))
w=list(q)
print(w)
print(type(w))
w.append(4)
print(w)
