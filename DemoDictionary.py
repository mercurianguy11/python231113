# DemoDictionary.py

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# dictionary => key:value
color = {"apple":"red", "banana":"yellow"}
print(color)

color["cherry"] = "red"
print(color)

for item in color.items():
    print(item)

for k, v in color.items():
    print(k,v)   # k = key, v = value

# dictionary 는 맵핑구조 (key 중심)
# del -> delete, def -> define (축약어)
del color["cherry"]
print(color)

color.clear()
print(color)

# 방아쇠수지증후군 앱코 알리익스프레스

device = {"아이폰":5, "아이패드":10, "윈도우타블렛":20}
print("lenth of device")
print(len(device))

print("print device")
print(device)

#검색 
print("value of 아이폰")
print(device["아이폰"])

#입력
print("add dictionary 맥북")
device["맥북"]=15
print(device)

#삭제
print("delete dictionary 아이패드")
del device["아이패드"]
print(device)

#수정
print("modified dictionary 아이패드")
device["아이폰"]=6
print(device)

# for 구문
for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)

print(device.keys())
print(device.values())
print("아이폰" in device)
print("테스트" not in device)

# Pass By Reference 
print("Pass By Reference")
d=device
print(d)
device["아이폰"]=7
print(d)

for key in device.keys():
    print(key)

for value in device.values():
    print(value)

for item in device.items():
    print(item)


#전화번호 저장
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" not in phone)

#참조를 전달
p = phone
p["kang"] = "1234"
print(phone)
print(p)
print(id(phone))  # id() 객체를 구분할수 있는 고유값
print(id(p))

print("---------- test bool ####1 ----------")
isRight = True
print(type(isRight))    
print(1>2)
print(1==2)
print(1!=2)
print("---------- test bool ####2 ----------")
print(bool(0))  # 숫자가 0 아니면 거짓
print(bool(1))
print(bool(-3))
print(bool([])) # 값이 없으면 거짓
print(bool([1,2,3]))
print(bool("test")) 
print(bool(None))
print(True and True and False)
print(True and True and True)
print(True or False or False) # True 가 하나만 있어도 or 는 True
print("---------- 산술연산 ----------")
print(2**2)
print(2**3)
print(5%2)
print(5//2) # 정수값
print(3+5)
print(3+5.0) # 정수 + 실수 => 실수
print(5/2) # 버전에 따라 다르다 : 실수 or 정수

