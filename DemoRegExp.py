# DemoRegExp.py

# ex ) 메일 : ~@~, 년도 : 2024(4자리), 우편번호 : 41200(5자리) 등등...
# 정규식 표현 ChatGPT에게 물어봐라...

# 정규표현식(re) 모듈: 정규표현식은 특정한 규칙을 가진 문자열을 표현하는데 사용되는 형식 언어이다. 
# . : 개행문자를 제외한 문자 1자를 나타낸다.
# ^ : 문자열을 시작을 나타낸다. 예를 들면 ^app는 app로 시작되는 패턴의 문자열을 가져온다. (캐롯)
# $ : 문자열의 종료를 나타낸다. 예를 들면 ful$는 ful로 끝나는 패턴의 문자열을 가져온다.  
# [] : 문자의 집합을 나타낸다. 예를 들면 [abcd]는 ‘a’, ‘b’, ‘c’, ‘d’ 중 한 문자와 매칭된다. [a-z]는 알파벳 소문자가 와야하며 [0-9]는 숫자만 와야 한다. 
# | : A|B와 같이 ‘A’ 또는 ‘B’를 나타낸다. 
# () : 괄호 안에 정규식을 그룹으로 만든다. 예를 들면 전화번호인 경우 (02)-(3429)-(5000)이라면 첫번째 그룹과 두번째,세번째 그룹을 분리해서 가져올 수 있다. 
# * : 문자가 0회 이상 반복됨을 나타낸다. 정리하면 0~N번 출현횟수를 말한다. 
# + : 문자가 1회 이상 반복됨을 나타낸다. 정리하면 1~N번 출현횟수를 말한다.  
# ? : 문자가 0 혹은 1회 반복됨을 나타낸다.
# {m} : 문자가 m회 반복됨을 나타낸다. \d{4}는 숫자가 연속으로 4자리 오는 경우를 말한다. 
# {m,n} : 문자가 m회부터 n회까지 반복되는 모든 경우를 나타낸다. \d{3,4}는 숫자가 3자리 또는 4자리까지 오는 경우를 말한다. 
# {m,} 문자가 m회부터 무한 반복되는 모든 경우를 나타낸다.  


# 정규표현식 예제 - 패턴....
# 정규식 ‘app.e’는 ‘apple’, ‘appLe’, ‘app-e’, ‘app e’가 매칭된다. 
# 정규식 ‘^app’는 ‘apple and orange’는 매칭되지만 ‘orange and apple’는 매칭되지 않는다.
# 정규식 ‘ple$’는 ‘orange and apple’는 매칭되지만 ‘apple and orange’는 매칭되지 않는다. 
# 정규식 ‘appl[a-z]’은 ‘apple’, ‘applz’와 같이 가장 마지막에 소문자가 오는 경우는 매칭된다. 
# 정규식 ‘appl[^a-z]’은 위와 반대로 마지막에 소문자가 오는 경우를 제외한 모든 경우에 매칭된다. 
# 정규식 ‘ap*le’는 ‘ale’, ‘aple’, ‘apppple’와 같이 p가 0회 이상 반복되는 모든 경우와 매칭된다(*는 0회 이상 반복)
# 정규식 ‘ap+le’는 ‘aple’, ‘appple’와 매칭되지만 ‘ale’는 매칭되지 않는다(+는 1회 이상 반복)
# 정규식 ‘ap?le’는 ‘ale’, ‘aple’와 매칭되지만 ‘apple’, ‘appple’와는 매칭되지 않는다(0회 또는 1회 반복)


# 확장 문자열: 이스케이프 문자열도 정의되어 있다.
# \w : 유니코드인 경우 숫자, 밑줄을 포함하는 모든 언어의 표현 가능한 문자 wide cahr
# \d : 유니코드인 경우 [0-9]를 포함하는 모든 숫자
# \s : 유니코드인 경우 [\t\n\r\f\v]를 포함하는 공백 문자
# \b : 단어의 시작과 끝의 빈 공백

# re 모듈 함수: 
# re.search(pattern, string[, flags]): string 전체에 대해 pattern이 존재하는지 검사해 MatchObject 인스턴스를 반환한다. 
# re.match(pattern, string[, flags]): string이 시작하는 부분부터 pattern이 존재하는지 검사해서 MatchObject인스턴스를 반환한다. 
# re.compile(pattern[, flags]): pattern을 컴파일해서 정규 표현식 객체를 반환한다.  미리 컴파일.... 검색 속도를 빠르게 한다..


# re모듈의 함수 사용:
# 문자열 검색을 할 때 두 함수 모두 첫 인자로 찾고자 하는 패턴을, 두 번째 인자로 검색 대상 문자열을 받아들인다. 

#정규표현식을 사용하는 경우
import re

print(re.match("[0-9]*th","35th"))
print(re.search("[0-9]*th","35th"))

# 두 함수의 다른 점은 re.match() 함수는 대상 문자열의 시작부터 검색하지만 
# re.search()함수는 대상 문자열 전체를 대상으로 검색한다는 것이다.  

# result = re.match("[0-9]*th","  35th")
# print(result)
# print(result.group())

# result = re.match("[0-9]*th","  35th")
# print(result)
# print(result.group())

print(bool(re.match("[0-9]*th","  35th")))
print(bool(re.search("[0-9]*th","  35th")))

print(bool(re.match("ap","this is apple")))
print(bool(re.search("ap","this is apple")))

print(bool(re.search("app.e","app3e")))
print(bool(re.search("app.e","app32e")))
print(bool(re.search("^app","apple and orange")))
print(bool(re.search("^app","orange and apple")))
print(bool(re.search("app$","apple and orange")))
print(bool(re.search("app$","orange and apple")))
print(bool(re.search("appl[a-z]","apple")))
print(bool(re.search("appl[a-z]","applE")))
print(bool(re.search("appl[^a-z]","apple")))
print(bool(re.search("appl[^a-z]","applE")))
print(bool(re.search("ap*le","ale")))
print(bool(re.search("ap*le","appppple")))
print(bool(re.search("ap+le","ale")))
print(bool(re.search("ap+le","appppple")))
print(bool(re.search("ap?le","ale")))
print(bool(re.search("ap?le","appppple")))
print(bool(re.search("ap{2}le","apple")))
print(bool(re.search("ap{2}le","appple")))
print(bool(re.search("ap{2,3}le","appple")))
print(bool(re.search("ap{2,3}le","apppple")))
print(bool(re.search("ap{2,}le","apppple")))



# 일반적인 검색
result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

# # 정확하게 일치
result = re.match("[0-9]*th","35th")
print(result)
print(result.group())


result = re.search("\d{4}","올해는 2023년")
print(result.group())  # 찾은 문자열만 보여준다.

result = re.search("\d{5}","우리동네는 51200")
print(result.group())

