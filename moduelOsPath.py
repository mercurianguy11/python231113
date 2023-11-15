# moduelOsPath.py

# 파일 입출력 기능을 이용해서 파일을 생성하거나 기존 파일을 관리할 수 있다.  
# from os.path import *를 실행하고 사용한다. 
# abspath(‘tmp’) : 현재 경로를 prefix로 해서 입력 받은 경로를 절대 경로로 바꿔서 반환한다.
# basename(path) : 입력 받은 경로의 기본 이름(base name)을 반환한다. 
# exists(path) : 입력 받은 경로가 존재하면 True를 리턴 한다. 
# isfile(), isdir(): 입력받은 파일이나 경로가 파일인지 폴더인지의 여부를 리턴한다. 
# getctime(path) : 입력 받은 경로에 대한 생성 시간을 반환한다. 
# getsize(path) : 입력 받은 경로에 대한 바이트 단위의 파일크기를 반환한다. 
# join(path1[, path2[, …]]) : 해당 OS형식에 맞게 입력 받은 경로를 연결한다. 
# normpath(path) : 해당 OS에 맞게 입력받은 경로의 문자열을 정규화 한다. 

from os.path import *
import glob

print(dir())
print(dir(glob))
fName = "C:\\Python310\\python.exe"
dName = "C:\\Python310"
tFile = "readme.txt"
print(isfile(fName))
print(isdir(fName))
print(isdir(dName))
print(abspath(tFile))
print(basename(fName))
print(exists(fName))
print(getsize(fName))

if exists(fName):
    print("#### {0} 파일크기 : {1} KB ####".format(fName, getsize(fName)))
else:
    print("#### 파일 없음 ####")


result = glob.glob("C:\\work\\*.py")
for item in result:
    print(basename(item))
    # print(item) ## 절대경로 

# https://wikidocs.net/book/5445 ->  점프 투 파이썬 - 라이브러리 예제 편   