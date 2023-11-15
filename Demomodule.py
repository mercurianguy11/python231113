# Demomodule.py
# import sampleset
# sampleset
# <module 'sampleset' from 'C:\\Python310\\lib\\sampleset.py'>
# dir(sampleset)
# ['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__builtins__', '__cached__', '__doc__', '__file__', 
# '__intersectSC', '__loader__', '__name__', '__package__', '__spec__', 'cache', 'cached_property', 
# 'cmp_to_key', 'difference', 'intersect', 'lru_cache', 'partial', 'partialmethod', 'reduce', 'singledispatch', 
#'singledispatchmethod', 'total_ordering', 'union', 'update_wrapper', 'wraps']


# 모듈 만들기: 파이썬에는 많은 내장 모듈이 있지만 사용자가 직접 모듈을 생성할 수 있다. 
# 합집합, 차집합을 구하는 간단한 집합 관련 모듈을 만들어서 
# c:\python310\lib에 복사하면 된다. 

# 모듈 선언 4가지 스타일(개인의 취향) 
# 1. import sampleset : 이름충돌을 피하기 위해 방을 만들고 사용 - 방이름을 써야함 ex) sampleset.union(a,b)
# 2. from <모듈> import <어트리뷰트> - ex) from sampleset import union -> union([1,2,3], [3,4,5]) : 쉽게 쓰겠다... sampleset 쓸필요 없음.
# 3. from sampleset import * : sampleset 모듈에 모든 함수를 가져옴 -> __로 시작하는 어트리뷰트를 제외하고 모든 어트리뷰트를 현재의 이름공간으로 임포트한다.
# 4. import testmodule as t1

# examples...
# 1. import sampleset
# 2. from sampleset import union
# 3. from sampleset import *
# 4. import testmodule as t1

# restart shell : ctrl + F6

# 1. import sampleset

# import sampleset
# sampleset
# <module 'sampleset' from 'C:\\Python310\\lib\\sampleset.py'>
# dir(sampleset)
# ['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__builtins__', '__cached__', '__doc__', '__file__', '__intersectSC', '__loader__', '__name__', '__package__', '__spec__', 'cache', 'cached_property', 'cmp_to_key', 'difference', 'intersect', 'lru_cache', 'partial', 'partialmethod', 'reduce', 'singledispatch', 'singledispatchmethod', 'total_ordering', 'union', 'update_wrapper', 'wraps']
# a=[1,2,3]
# b=[3,4,5]
# sampleset.union(a,b)
# [1, 2, 3, 4, 5]
# sampleset.intersect(a,b)
# [3]

# 2. from sampleset import union

# from sampleset import union
# dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'union']
# union([1,2,3],[3,4,5])
# [1, 2, 3, 4, 5]
# intersect([1,2,3],[3,4,5])
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     intersect([1,2,3],[3,4,5])
# NameError: name 'intersect' is not defined

# 3. from sampleset import *

# dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
# from sampleset import *
# dir()
# ['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'cache', 'cached_property', 'cmp_to_key', 'difference', 'intersect', 'lru_cache', 'partial', 'partialmethod', 'reduce', 'singledispatch', 'singledispatchmethod', 'total_ordering', 'union', 'update_wrapper', 'wraps']
# union([1,2,3],[3,4,5])
# [1, 2, 3, 4, 5]
# intersect([1,2,3],[3,4,5])
# [3]
# difference([1,2,3],[3,4,5])
# [1, 2, 4, 5]


import sampleset

# 모듈 로딩한 디렉토리 출력
print(sampleset)

print(dir(sampleset))
setA=[1,2,3]
setB=[3,4,5]
print(sampleset.union(setA, setB))
