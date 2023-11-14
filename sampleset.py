# 함수(3장) : 1개 기능
# 클래스(4장) : N개 변수 + M개 메서드
# 모듈(4장) : 1개 파일인데 여러개의 함수 클래스로 구성 -> 규모와 복잡도 증가

# 메모리에 올려줘...
# __ 첨부되는 함수 정의 -> 순결하다. 외부에서 보이지 않음

# help("modules")
from functools import *

def intersect(*ar):
    return reduce(__intersectSC,ar)

def __intersectSC(listX, listY):
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    setList = []
    intersectSet = intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList


