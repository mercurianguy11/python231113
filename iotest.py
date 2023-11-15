# iotest.py

# str(int) : int -> string type 변환
x=0.2
print(x)
print(str(x))

# Error!!!!
# TypeError: can only concatenate str (not "int") to str
# url="http://www.credu.com/?page="+1
# print(url)

url="http://www.credu.com/?page="+str(2)
print(url)
print("\n")    

for i in range(1,11):
    url="http://www.credu.com/?page="+str(i)
    print(url)
print("\n")    
for x in range(1,6):
    print(x, "*", x,"=",x*x)
print("-----------3자리 오른쪽 정렬-----------")    
for x in range(1,6):
    print(x, "*", x,"=",str(x*x).rjust(3))    # 3자리 오른쪽 정렬
print("-----------3자리 왼쪽 정렬-----------")       
for x in range(1,6):
    print(x, "*", x,"=",str(x*x).ljust(3))    # 3자리 왼쪽 정렬  
print("-----------5자리 0으로 채우기-----------")  
for x in range(1,6):
    print(x, "*", x,"=",str(x*x).zfill(5))    # 5자리 0으로 채우기      

print("{0:x}".format(10))  # hex format
print("{0:o}".format(10))  # octet format
print("{0:b}".format(10))  # binary format
print("{0:,}".format(150000)) # 3자리마다 , 구분
print("{0:e}".format(4/3))  # 지수 
print("{0:f}".format(4/3))  # 실수
print("{0:.2f}".format(4/3))  # 실수 2자리까지만

# 기능이 약함, pandas 라이브러리 활용 : read_csv(), read_excel()
# r : 읽기모드
# w : 쓰기모드
# a : 쓰기 + 이어쓰기 모드
# + : 읽기 + 쓰기모드
# b : 바이너리 모드
# t : 테스트 모드
# ex) rt, wt, a+
f = open("test.txt","wt") 
f.write("aaa\nbbb")
f.close()
f = open("test.txt") 
print(f.read())
f.close()
f.closed


