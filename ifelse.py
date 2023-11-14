# ifelse.py


# if 문 
# score=int(input("점수를 입력:"))  # int형 인자를 입력
# if 90 <= score <= 100:
#     grade="A"
# elif 80 <= score < 90:
#     grade="B"
# elif 70 <= score < 80:
#     grade="C"    
# else:
#     grade="D"

# print("등급은 ", grade)


# while 문
value=5
while value > 0:
    print("value is %d." % value)
    value-=1     # value = value - 1


# for 문
lst = ["apple", 100, 3.14]
print("### lst's length is",len(lst))
for item in lst:
    print(item, type(item))

d = {"apple":100, "orange":200, "banana":300}
print("### d's length is",len(d))
print("### d's length is",len(d.items()))

for item in d.items():  
    print(item)    

for k,v in d.items():  
    print(k,v)    



# range 함수 예제  
# range(start, end, step) : 수열의 생성
print(list(range(10)))
print(list(range(1,10)))
print(list(range(5,10)))
print(list(range(10,0,-1)))
print(list(range(10,20,2)))

lst = list(range(1,11))
print(lst)

years = list(range(2000,2024))
print(years)

days = list(range(1,32))
print(days)

print("----수동으로 반복------")
for i in range(10):
    print(i)


print("----break 구문------")
lst2 = [1,2,3,4,5,6,7,8,9,10]
for item in lst2:
    if item > 5:
        break
    print("Item:{0}".format(item))  # print("Item:%s" % item) 와 동일

print("break!\n")    

print("----continue 구문------")
for item in lst2:
    if item % 2 == 0:
        continue
    print("Item:%s" % item)
print("continue!\n")    


# list(), int(), str(), range() : 자주 사용하는 함수
print("----str 구문 연습------")
print(str(12345678))
print(str(12345678)[2])


print("----리스트함축------")
lst3 = [1,2,3,4,5,6,7,8,9,10]
print([i**2 for i in lst3])  # list 함축
print([i**2 for i in lst3 if i > 5])  # list 함축
t=("apple","banana","orange")
print([len(i) for i in t])
d={100:"apple", 200:"banana",300:"orange"}
print([v.upper() for v in d.values()])



print("----필터링함수------")
lst=[10,25,30]
iterL=filter(None, lst)
for item in iterL:
    print("Item:{0}".format(item))

## define getBiggerThan20 
def getBiggerThan20(i):
    return i>20
print("----필터링함수 : getBiggerThan20------")  # camel 표기 
iterL=filter(getBiggerThan20, lst)  # true 인것만 보여준다...
for item in iterL:
    print("Item:{0}".format(item))


print("----람다함수------")  # camel 표기 
iterL=filter(lambda a:a>20, lst)  # true 인것만 보여줘...
for item in iterL:
    print("Item:{0}".format(item))

print("----리스트 함축------")  # camel 표기 
print([i for i in lst if i > 20])  # list 함축      