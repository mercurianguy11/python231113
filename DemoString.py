# DemoString.py

# RPA (업무자동화, Robotic Process Automation) => 생성형 AI (자연어 코딩)
print(dir(str)) 

# str 은 기본 도구... import 할 필요 없다.
# 주요 함수 : capitalize, count, encode, endswith, find, format, index, 
# isalnum, isalpha, isdecimal, istitle, join, ljustm lower, replace, rjust, split, strip, upper, zfill + len()

# 첫문자를 대문자로 변경
print("python is powerful".capitalize()) 

# count(keyword, [start, [end]]): 특정구간 지정 가능
print("python is powerful".count("p"))  

# encode([encoding, [errors]]): 파이썬 3에서 str 클래스는 기본적으로 모두 유니코드이다 
# 참고 [] 는 optional 의미....

# endswith(postfix, [start, end]]): postfix로 문자열이 끝나면 True를 반환, 아니면 False를 반환. start, end를 지정하면 슬라이싱 한 효과
print("python is powerful".endswith("ful"))
print("python is powerful".endswith("ful",9))

# isalnum(), isdecimal(): 알파벳과 숫자로만 구성되었는지, 숫자로만 구성되어 있는지를 알려준다.   
print("MBC2580".isalnum())
print("2580".isdecimal())


# str 함수 연습
u = " spam and ham "
print("print u : ", end="")
print(u)
print("print u.strip() : ", end="")
print(u.strip())
print("print u.rstrip() : ", end="")
print(u.rstrip())
print("print u.lstrip() : ", end="")
print(u.lstrip())
print("print u.replace spam to spam egg : ", end="")
print(u.replace("spam","spam egg"))
result = u.split()
print("print u.split() : ", end="")
# result return 안받아서 spam egg 취환 저장 안됨!!!!
print(result) 
print("print :).join(result) : ", end="")
print(":)".join(result))

print("---실습---")
strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.startswith("py"))
print(strA.endswith("ful"))
print("---알파멧과 숫자로 구성---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("---str 함수 연습---")
data = "<<< spam and ham  >>>"
result = data.strip("<> ")  # return 을 받아야 저장한다 : "<", ">", " " 삭제....
print(data)
print(result)
result = result.replace("spam","spam egg") # 중요!! return 을 받아야 저장... :취환...
print("반환 결과")
print(result)
lst = result.split()
print(lst)
print("---다시 합치기---")
print(":)".join(lst))

# 구분자를 지정하는 경우
print("---구분자 지정---")
strC = "spam::egg::ham"
lstC = strC.split("::")
print(lstC)

# 반복문자열 생성
names = ["전우치","이순신", "박문수"]
for name in names:
    print("안녕하세요 {0}님 초겨울입니다.".format(name))
    print("="*40)  # 반복문자열 생성



