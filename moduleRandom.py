# moduleRandom.py

# 랜덤 모듈 : 임의의 정수, 실수를 생성하거나 시퀀스 객체 중 임의의 값을 선택하는 연산을 위해 랜덤 모듈을 제공한다. 
# random.seed([x]) : 임의 숫자 생성기의 초기화 작업을 한다.
# random.random() : 0.0 <= 1.0 사이의 임의의 float 숫자를 반환한다. 
# random.shuffle(x[, random]) : 입력 받은 시퀀스 객체를 섞는다. 
# random.sample(population, k) : 두 번째 인자 k개만큼의 아이템을 첫 번째 인자인 시퀀스나 셋 객체로부터 임의로 중복 없이 추출한다

import random
print(dir(random))
print("---- random.random() ------")
print(random.random())
print(random.random())
print("---- random.uniform() ------")
print(random.uniform(2,5))
print(random.uniform(1.0,5.0))
print("---- random.randrange ------")
listA = [random.randrange(20) for i in range(10)]
print(listA)
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---- random.sample ------")
print(random.sample(range(20),10))
print(random.sample(range(20),10))
print(random.sample(range(20),10))
print("---- lotto ------")
lotto = list(range(1,46))  ## 전역변수 list 와 중복 list -> listA로 전역변수 변경
print(lotto)
random.shuffle(lotto)
print(lotto)