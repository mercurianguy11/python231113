# demomath.py

# 파이썬은 다양한 모듈을 제공한다.
# 문자열(string), 날짜(date), 시간(time), 수학(math), 분수(fraction), 십진법(decimal), 랜덤(random), 파일(file), sqlite3, os, sys, threading, xml, http 등등 약 200개 정도의 다양한 모듈들이 존재한다. 
# 개발자가 필요하면 모듈을 작성해서 제공할 수 있다. 
# 내가 만든 모듈을 다른 개발자들에게 제공하거나 또는 제공 받을 수 있다. 

# python 은 키워드가 36개(예약어) + 내부 라이브러리(모듈, 패키지) 200개 정도 + 외부 라이브러리(10개)
# 구글 검색 : 파이썬 math 모듈
# https://wikidocs.net/21116


# import math
# dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math', 'times']
# dir(math)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 
# 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 
# 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 
# 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
# 'tan', 'tanh', 'tau', 'trunc', 'ulp']



import math

print(dir(math))
print(math.pow(2,10))
print(math.log(100))
print(math.factorial(5))
print(math.pi*2)
print(math.sin(math.degrees(90)))
print(math.cos(0))
print(math.sin(1))