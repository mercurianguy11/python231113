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


# file 입출력

# 기능이 약함, pandas 라이브러리 활용 : read_csv(), read_excel()
# r : 읽기모드
# w : 쓰기모드
# a : 쓰기 + 이어쓰기 모드
# + : 읽기 + 쓰기모드
# b : 바이너리 모드
# t : 테스트 모드
# ex) rt, wt, a+

print("------파일 입출력------") 
f = open("c:\\work\\test.txt","wt", encoding="utf-8") 

s1=f.write("첫번째라인\n두번째라인\n세번째라인\n")  # \n 개행문자
print("커서위치 : %d\n" % s1)
f.close()
f = open("c:\\work\\test.txt","rt", encoding="utf-8") 
print(f.read())  # 처음서부터 끝까지 읽는다.
f.close()
f.closed # 파일 닫았는지 확인하는 변수 if(!f.closed) f.close()

# 파일에 첨부(append, read, write)
f = open("c:\\work\\test.txt","a+", encoding="utf-8") 
s1=f.write("추가로 첨부하기\n")  # \n 개행문자
f.close()

f = open("c:\\work\\test.txt","rt", encoding="utf-8") 
print("f.read() : 처음서부터 끝까지 읽는다.")
print(f.read())  # 처음서부터 끝까지 읽는다.
print("f.seek(0) : 다시 처음")
f.seek(0)
result=f.readlines()
for item in result:
    print(item, end="")

# 다시 처음
print("f.seek(0) : 다시 처음")
f.seek(0)
print("f.readline() : 한줄씩 읽는다")
print(f.readline(), end="")
print("f.readline() : 한줄씩 읽는다")
print(f.readline(), end="")
f.close()


# 용도별 파일 처리 함수
# 1. read() => str변수(1~10)
# 2. readlines() => list변수(500줄) 
# 3. readline() => 500MB~1GB(Log, DataSet) : while 문
# 4. write() : 파일 쓰기 작업
# 5. tell() : 어디까지 읽고 썼는지 위치를 반환
# 6. seek() : 사용자가 원하는 위치로 파일 포인터 이동

f = open("c:\\work\\test.txt","rt", encoding="utf-8") 
while True:
    line = f.readline()
    print("-----readline file test---")
    print(line)
    if line == "":
        print("끝\n")
        break 

f.close()


# 파일에 첨부(append, read, write)
f = open("c:\\work\\test.txt","wt", encoding="utf-8") 
s1=f.write("새로작성!!!\n")  # \n 개행문자
f.close()

f = open("c:\\work\\test.txt","rt", encoding="utf-8") 
print(f.read())  # 처음서부터 끝까지 읽는다.
# 커서를 맨 앞으로 이동
f.close()


# 서식 지정
print("{0:x}".format(10))  # hex format
print("{0:o}".format(10))  # octet format
print("{0:b}".format(10))  # binary format
print("{0:,}".format(150000)) # 3자리마다 , 구분
print("{0:e}".format(4/3))  # 지수 
print("{0:f}".format(4/3))  # 실수
print("{0:.2f}".format(4/3))  # 실수 2자리까지만



