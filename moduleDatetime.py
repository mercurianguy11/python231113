# moduleDatetime.py

# 날짜시간(datetime) 모듈:
# class datetime.date : 일반적으로 사용되는 그레고리안 달력의 년, 월, 일을 나타낸다.
# class datetime.time : 시간을 시, 분, 초, 마이크로 초, 시간대로 나타낸다.
# class datetime.datetime : date 클래스와 time클래스의 조합으로 년, 월, 일, 시, 분, 초, 마이크로 초, 시간대 정보를 나타낸다.
# class datetime.timedelta : 두 날짜 혹은 시간 사이의 기간을 표현한다. 

#datetime.date(2023, 5, 1)


from datetime import *
print(dir(datetime))

print(date(2023,5,1))
print(date(2023,10,1))
print(date.today())


d3 = date(2023,12,5)
print(d3)
d4 = date.today()
print(d4)
d5 = datetime.now()
print(d5)

d1 =  date.today()
print(d1)
d2 = timedelta(days=100)
print(d1+d2)
